"""Initial migration

Revision ID: 467e82965cd5
Revises: 
Create Date: 2024-11-13 22:51:47.662335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '467e82965cd5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('profile_picture', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('drivers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('id_no', sa.String(length=20), nullable=False),
    sa.Column('driving_license_no', sa.String(length=20), nullable=False),
    sa.Column('profile_picture', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('driving_license_no'),
    sa.UniqueConstraint('id_no')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('distance', sa.Float(), nullable=False),
    sa.Column('loader_number', sa.Integer(), nullable=False),
    sa.Column('loader_cost', sa.Float(), nullable=False),
    sa.Column('from_location', sa.String(length=100), nullable=False),
    sa.Column('to_location', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('driver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['driver_id'], ['drivers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('body_type', sa.String(length=50), nullable=False),
    sa.Column('plate_no', sa.String(length=20), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('driver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['driver_id'], ['drivers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('plate_no')
    )
    op.create_table('rides',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('distance', sa.Float(), nullable=False),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('loader_cost', sa.Float(), nullable=False),
    sa.Column('from_location', sa.String(length=100), nullable=False),
    sa.Column('to_location', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rating_score', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('ride_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['ride_id'], ['rides.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ratings')
    op.drop_table('rides')
    op.drop_table('vehicles')
    op.drop_table('orders')
    op.drop_table('drivers')
    op.drop_table('customers')
    # ### end Alembic commands ###
