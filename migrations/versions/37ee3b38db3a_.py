"""empty message

Revision ID: 37ee3b38db3a
Revises: 32e35f6f792b
Create Date: 2022-09-28 13:50:40.895853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37ee3b38db3a'
down_revision = '32e35f6f792b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('number', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
