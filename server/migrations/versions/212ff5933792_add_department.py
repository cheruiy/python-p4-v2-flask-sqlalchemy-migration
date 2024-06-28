"""add Department

Revision ID: 212ff5933792
Revises: 7038755676c5
Create Date: 2024-06-28 11:51:33.830798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '212ff5933792'
down_revision = '7038755676c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
