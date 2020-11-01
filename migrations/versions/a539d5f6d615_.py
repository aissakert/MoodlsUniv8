"""empty message

Revision ID: a539d5f6d615
Revises: 125f94da118c
Create Date: 2020-10-31 03:01:03.827704

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a539d5f6d615'
down_revision = '125f94da118c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('administrateur', 'is_admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('administrateur', sa.Column('is_admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
