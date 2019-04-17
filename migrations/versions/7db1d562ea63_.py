"""empty message

Revision ID: 7db1d562ea63
Revises: 9fb652969211
Create Date: 2019-04-15 22:38:44.422206

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7db1d562ea63'
down_revision = '9fb652969211'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    op.drop_constraint('sheet_iteration_key', 'sheet', type_='unique')
    op.drop_column('sheet', 'iteration')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sheet', sa.Column('iteration', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_unique_constraint('sheet_iteration_key', 'sheet', ['iteration'])
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('values', postgresql.ARRAY(sa.NUMERIC()), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###