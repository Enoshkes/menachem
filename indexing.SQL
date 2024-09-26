explain analyze select * from developer where id in (
	select developer_id from developer_companies
	where company_id in (select id from company)
)

create index idx_developer_id on developer_companies(developer_id)
create index idx_developer_id on developer_companies(developer_id)
