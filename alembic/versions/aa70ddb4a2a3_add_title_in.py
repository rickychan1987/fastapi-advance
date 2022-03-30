"""add title in

Revision ID: aa70ddb4a2a3
Revises: 09e0b117b282
Create Date: 2022-03-31 01:18:34.064964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa70ddb4a2a3'
down_revision = '09e0b117b282'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
