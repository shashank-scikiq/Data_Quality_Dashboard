import streamlit as st
from get_data import od_dq, run_stmt
from sqlalchemy import Select, func
from datetime import date


@st.cache_data
def get_date_range():
	date_range = (
		Select(func.min(od_dq.c.ord_date), func.max(od_dq.c.ord_date))
	)
	dt_rng = run_stmt(date_range)[0]
	return dt_rng[0], dt_rng[1]


min_ord_date = get_date_range()[0]
max_ord_date = get_date_range()[1]


@st.cache_data
def load_cancelled_orders(dt_val: date, total=0):
	cancelled = (
		Select(od_dq.c.seller_np, od_dq.c.null_cans_code, od_dq.c.total_canceled_orders)
		.where(od_dq.c.total_canceled_orders > 0)
		.where(od_dq.c.null_cans_code > 0)
		.where(od_dq.c.ord_date == dt_val)
		.order_by(od_dq.c.null_cans_code.desc())
	)
	return run_stmt(cancelled, total)


@st.cache_data
def load_missing_pc(dt_val: str, col_name: str, total=0):
	col_ = getattr(od_dq.c, col_name)
	missing_col = (
		Select(
			od_dq.c.seller_np,
			col_,
			od_dq.c.total_orders)
		.where(col_ > 0)
		.where(od_dq.c.ord_date == dt_val)
		.order_by(col_.desc())
	)
	return run_stmt(missing_col, total)


@st.cache_data
def curr_date():
	curr_dt = (
		Select(func.max(od_dq.c.curr_date))
	)
	return run_stmt(curr_dt)


@st.cache_data
def get_columns():
	return od_dq.columns.keys()


@st.cache_data
def get_sellers(dt_val: str):
	sellers = (
		Select(
			od_dq.c.seller_np).distinct().where(
			od_dq.c.ord_date == dt_val)
			)
	return run_stmt(sellers)
