"""empty message

Revision ID: ccd7cf7dbc60
Revises: 81604100b94b
Create Date: 2023-10-23 23:56:35.794504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd7cf7dbc60'
down_revision = '81604100b94b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=300), nullable=False),
    sa.Column('content', sa.String(length=1000), nullable=False),
    sa.Column('todo_id', sa.Integer(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['todo_id'], ['todolist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
