"""Profile

Revision ID: bb1f5e515779
Revises: 7529f95fdf11
Create Date: 2018-09-15 16:07:32.801765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb1f5e515779'
down_revision = '7529f95fdf11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('comment_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'comments', ['comment_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'comment_id')
    # ### end Alembic commands ###
