"""empty message

Revision ID: af05a6e87f63
Revises: 0524d3489e2d
Create Date: 2023-11-09 20:16:18.479295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af05a6e87f63'
down_revision = '0524d3489e2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    with op.batch_alter_table('todolist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todolist', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###
