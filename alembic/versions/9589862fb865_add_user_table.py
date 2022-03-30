"""add user table

Revision ID: 9589862fb865
Revises: aa70ddb4a2a3
Create Date: 2022-03-31 01:40:24.000037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9589862fb865'
down_revision = 'aa70ddb4a2a3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
