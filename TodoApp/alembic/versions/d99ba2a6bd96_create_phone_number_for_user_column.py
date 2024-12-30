"""Create phone number for user column

Revision ID: d99ba2a6bd96
Revises: 237e48fad6d8
Create Date: 2024-12-22 09:03:44.850568

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd99ba2a6bd96'
down_revision: Union[str, None] = '237e48fad6d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable = True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
