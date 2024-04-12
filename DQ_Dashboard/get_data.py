from sqlalchemy import create_engine, MetaData, Table, Column, Date, String, BIGINT
from sqlalchemy import Select

engine = create_engine("postgresql+psycopg://postgres:password@localhost:5432/postgres")
meta = MetaData()
meta.reflect(bind=engine, schema="staging_all")

od_dq = Table(
	"od_dq_nhm",
	meta,
	Column("curr_date", Date, nullable=True),
	Column("ord_date", Date, nullable=True),
	Column("seller_np", String(255), nullable=True),
	Column("null_fulfilment_id", BIGINT, nullable=True),
	Column("null_net_tran_id", BIGINT, nullable=True),
	Column("null_qty", BIGINT, nullable=True),
	Column("null_itm_fulfilment_id", BIGINT, nullable=True),
	Column("null_del_pc", BIGINT, nullable=True),
	Column("null_created_date_time", BIGINT, nullable=True),
	Column("null_domain", BIGINT, nullable=True),
	Column("null_del_cty", BIGINT, nullable=True),
	Column("null_cans_code", BIGINT, nullable=True),
	Column("null_cans_dt_time", BIGINT, nullable=True),
	Column("null_ord_stats", BIGINT, nullable=True),
	Column("null_fulfil_status", BIGINT, nullable=True),
	Column("null_itm_cat", BIGINT, nullable=True),
	Column("null_cat_cons", BIGINT, nullable=True),
	Column("null_sell_pincode", BIGINT, nullable=True),
	Column("null_prov_id", BIGINT, nullable=True),
	Column("null_itm_id", BIGINT, nullable=True),
	Column("null_sell_np", BIGINT, nullable=True),
	Column("null_net_ord_id", BIGINT, nullable=True),
	Column("null_sell_cty", BIGINT, nullable=True),
	Column("total_orders", BIGINT, nullable=True),
	Column("total_canceled_orders", BIGINT, nullable=True),
	schema="staging_all",
	extend_existing=True
)


def run_stmt(to_run, cnt=0):
	stmt = (
		to_run
	)
	with engine.connect() as conn:
		if cnt > 0:
			result = conn.execute(stmt).fetchmany(cnt)
		else:
			result = conn.execute(stmt).fetchall()
	return result


if __name__ == "__main__":
	# print(cancelled_orders())
	engine.dispose()
