"""empty message

Revision ID: ceab369b095c
Revises: 70b6160cf88c
Create Date: 2022-09-27 21:02:51.549764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceab369b095c'
down_revision = '70b6160cf88c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('money', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'money')
    # ### end Alembic commands ###