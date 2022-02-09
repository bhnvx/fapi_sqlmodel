"""Instalize Base Entity

Revision ID: a56019423258
Revises: 
Create Date: 2022-02-09 16:00:10.595286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a56019423258'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('User',
                    sa.Column('id', sa.String(length=32), nullable=False),
                    sa.Column('username', sa.String(length=32), nullable=False),
                    sa.Column('password', sa.String(length=128), nullable=False),
                    sa.Column('created_on', sa.DateTime),
                    sa.PrimaryKeyConstraint('id'),
                    )
    op.create_index(op.f('ix_User_id'), 'id', ['id'], unique=True)
    op.create_index(op.f('ix_User_username'), 'username', ['username'], unique=True)
    op.create_index(op.f('ix_User_password'), 'password', ['password'], unique=False)
    op.create_index(op.f('ix_User_created_on'), 'created_on', ['created_on'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_User_created_on'), table_name='created_on')
    op.drop_index(op.f('ix_User_password'), table_name='password')
    op.drop_index(op.f('ix_User_username'), table_name='username')
    op.drop_index(op.f('ix_User_id'), table_name='id')
    op.drop_table('User')
