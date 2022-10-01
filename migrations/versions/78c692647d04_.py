"""empty message

Revision ID: 78c692647d04
Revises: d7fad6464158
Create Date: 2022-10-01 15:46:06.019656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78c692647d04'
down_revision = 'd7fad6464158'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('info', sa.String(length=120), nullable=True),
    sa.Column('made_by', sa.String(length=30), nullable=True),
    sa.Column('made_in', sa.String(length=30), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=True),
    sa.Column('id_root', sa.Integer(), nullable=True),
    sa.Column('is_user', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('device')
    # ### end Alembic commands ###