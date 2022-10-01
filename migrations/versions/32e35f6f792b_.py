"""empty message

Revision ID: 32e35f6f792b
Revises: effea3a4c5dd
Create Date: 2022-09-28 13:03:19.669900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32e35f6f792b'
down_revision = 'effea3a4c5dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('name', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'name')
    # ### end Alembic commands ###