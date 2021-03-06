"""create all tabels

Revision ID: bc6db77c1f8a
Revises: 
Create Date: 2017-07-19 16:46:58.683601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc6db77c1f8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('investor',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('investor_id', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('investor_id')
    )
    op.create_table('page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('pagepath', sa.String(length=255), nullable=False),
    sa.Column('functionDescription', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('functionDescription'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('pagepath')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rolename', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rolename')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    op.create_table('contract_prc',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('investor_id', sa.String(length=255), nullable=False),
    sa.Column('contract_name', sa.String(length=255), nullable=False),
    sa.Column('BuyPositionLimit', sa.INTEGER(), nullable=False),
    sa.Column('CancelTimesLimit', sa.INTEGER(), nullable=False),
    sa.Column('LotSize', sa.INTEGER(), nullable=False),
    sa.Column('MinPriceRangeLimit', sa.INTEGER(), nullable=False),
    sa.Column('OpenOrderLimit', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['investor_id'], ['investor.investor_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contract_name'),
    sa.UniqueConstraint('investor_id'),
    sa.UniqueConstraint('investor_id', 'contract_name')
    )
    op.create_table('investor_prc',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('investor_id', sa.String(length=255), nullable=True),
    sa.Column('MarginOccupyCheckEnable', sa.Boolean(), nullable=True),
    sa.Column('MarginPercentValue', sa.INTEGER(), nullable=True),
    sa.Column('PositionCheckEnable', sa.Boolean(), nullable=True),
    sa.Column('RejectAllSell', sa.Boolean(), nullable=True),
    sa.Column('RejectAllBuy', sa.Boolean(), nullable=True),
    sa.Column('PriceTickCheckEnable', sa.Boolean(), nullable=True),
    sa.Column('PriceRangeCheckEnable', sa.Boolean(), nullable=True),
    sa.Column('RejectInvalidTickSizeEnable', sa.Boolean(), nullable=True),
    sa.Column('RejectInvalidLotSizeEnable', sa.Boolean(), nullable=True),
    sa.Column('QSThrottleEnable', sa.Boolean(), nullable=True),
    sa.Column('QSThrottleInterval', sa.INTEGER(), nullable=True),
    sa.Column('QSOrdersPerInterval', sa.INTEGER(), nullable=True),
    sa.Column('TotalThrottleEnable', sa.Boolean(), nullable=True),
    sa.Column('TotalThrottleInterval', sa.INTEGER(), nullable=True),
    sa.Column('TotalOrdersPerInterval', sa.INTEGER(), nullable=True),
    sa.Column('PriceCheckEnable', sa.Boolean(), nullable=True),
    sa.Column('allowMktOrders', sa.Boolean(), nullable=True),
    sa.Column('RestrictTrading', sa.Boolean(), nullable=True),
    sa.Column('MaxQtyEnable', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['investor_id'], ['investor.investor_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('permission_authentication',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('roleID', sa.INTEGER(), nullable=True),
    sa.Column('target', sa.String(length=255), nullable=True),
    sa.Column('display', sa.Boolean(), nullable=False),
    sa.Column('edit', sa.Boolean(), nullable=False),
    sa.Column('args', sa.TEXT(), nullable=True),
    sa.Column('willcheck', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['roleID'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('roleID', 'target')
    )
    op.create_table('rprelationship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roleID', sa.Integer(), nullable=True),
    sa.Column('pageTree', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['roleID'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pageTree'),
    sa.UniqueConstraint('roleID')
    )
    op.create_table('urrelationship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('roleID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['roleID'], ['role.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('urrelationship')
    op.drop_table('rprelationship')
    op.drop_table('permission_authentication')
    op.drop_table('investor_prc')
    op.drop_table('contract_prc')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('page')
    op.drop_table('investor')
    # ### end Alembic commands ###
