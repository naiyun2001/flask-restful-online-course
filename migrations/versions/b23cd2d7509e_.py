"""empty message

Revision ID: b23cd2d7509e
Revises: 1301713599c0
Create Date: 2022-09-07 17:05:38.756849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b23cd2d7509e'
down_revision = '1301713599c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('demo', sa.Column('mobile', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('demo', 'mobile')
    # ### end Alembic commands ###
