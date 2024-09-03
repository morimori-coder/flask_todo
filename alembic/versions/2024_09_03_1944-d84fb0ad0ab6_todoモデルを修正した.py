"""TODOモデルを修正した

Revision ID: d84fb0ad0ab6
Revises: b0b8157cbf4f
Create Date: 2024-09-03 19:44:22.259171

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd84fb0ad0ab6'
down_revision: Union[str, None] = 'b0b8157cbf4f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'status',
               existing_type=sa.VARCHAR(length=10, collation='Japanese_CI_AS'),
               type_=sa.Boolean(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'status',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=10, collation='Japanese_CI_AS'),
               nullable=False)
    # ### end Alembic commands ###
