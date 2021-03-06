"""add root user

Revision ID: 00b12cb2791c
Revises: 
Create Date: 2017-06-09 13:47:25.221997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00b12cb2791c'
down_revision = None
branch_labels = None
depends_on = None

from app import db,models

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pagepath', sa.String(length=255), nullable=False),
    sa.Column('functionDescription', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('functionDescription'),
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
    root = models.User('root', '123456')
    db.session.add(root)
    db.session.commit()

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('urrelationship')
    op.drop_table('rprelationship')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('page')
    # ### end Alembic commands ###
