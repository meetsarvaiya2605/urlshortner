"""initial

Revision ID: 915ca29ea81a
Revises: 
Create Date: 2025-03-06 12:06:20.696031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '915ca29ea81a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    op.drop_table('userss')
    op.drop_table('sales')
    op.drop_table('bottles')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('lastname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone_number', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('email_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email_id', name='users_email_id_key'),
    sa.UniqueConstraint('lastname', name='users_lastname_key'),
    sa.UniqueConstraint('phone_number', name='users_phone_number_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('bottles',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('bottles_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('bottle_capacity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('bottle_amount', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='bottles_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='bottles_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('sales',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('currency', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('notification', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='sales_pkey')
    )
    op.create_table('userss',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('bottle_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('firstname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('lastname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('set_goal', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('current_status', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('notification_on', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('notification_off', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['bottle_id'], ['bottles.id'], name='userss_bottle_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='userss_pkey'),
    sa.UniqueConstraint('email_id', name='userss_email_id_key')
    )
    op.create_table('customer',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='customer_pkey')
    )
    # ### end Alembic commands ###
