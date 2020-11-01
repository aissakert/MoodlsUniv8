"""empty message

Revision ID: 850c83bc452c
Revises: 521a59ca8c78
Create Date: 2020-10-31 21:18:22.260890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '850c83bc452c'
down_revision = '521a59ca8c78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('etudiant', sa.Column('num_etud', sa.String(length=60), nullable=True))
    op.create_index(op.f('ix_etudiant_num_etud'), 'etudiant', ['num_etud'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_etudiant_num_etud'), table_name='etudiant')
    op.drop_column('etudiant', 'num_etud')
    # ### end Alembic commands ###
