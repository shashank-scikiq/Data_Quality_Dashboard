import streamlit as st
import models as mdl
from datetime import timedelta

#  Dashboard Elements
# ====================================================

# Overview of data fields and % daTA MISSING,
# trend

min_ord_date = mdl.get_date_range()[0]
max_ord_date = mdl.get_date_range()[1]

with st.sidebar:
	dt = st.date_input("Select a Date", value=max_ord_date, min_value=min_ord_date, max_value=max_ord_date)
	option_comp = st.selectbox("Column Name ", [x for x in mdl.get_columns()
												if x.__contains__('null')], index=8)
	seller_name = st.selectbox("Seller NP", [x[0] for x in mdl.get_sellers(dt)])

st.title('OD Data Quality Report')
st.write(f"""
For : {dt.strftime("%Y-%m-%d")}
""")

st.write(option_comp)

tab_hm, tab_det, tab_can, tab_trend = st.tabs(["Column Heatmap", "Detail Completed", "Detail Cancelled", "Trend"])

#  Detailed Heatmap
# ====================================================================================


#  Detailed Completed
# ====================================================================================

with tab_det:
	st.write(f"Sellers with Highest Missing {option_comp}.")
	missing_col = mdl.load_missing_pc(dt_val=dt, col_name=option_comp, total=0)

	if missing_col:
		col1, col2, col3 = st.columns(3)

		try:
			col1.metric(label=missing_col[0][0],
						value=str(round((missing_col[0][1] / missing_col[0][2]) * 100, 2)) + "%",
						delta="5% Threshold")
		except:
			pass

		try:
			col2.metric(label=missing_col[1][0],
						value=str(round((missing_col[1][1] / missing_col[1][2]) * 100, 2)) + "%",
						delta="5% Threshold")
		except:
			pass

		try:
			col3.metric(label=missing_col[2][0],
						value=str(round((missing_col[2][1] / missing_col[2][2]) * 100, 2)) + "%",
						delta="5% Threshold")
		except:
			pass

		st.table(missing_col)
	else:
		st.write(f"{option_comp} has 'no missing value' for {dt}.")
