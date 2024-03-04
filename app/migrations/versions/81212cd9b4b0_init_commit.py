"""Init commit

Revision ID: 81212cd9b4b0
Revises: 
Create Date: 2024-03-02 18:59:01.663493

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81212cd9b4b0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('worker',
    sa.Column('worker_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('pass_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('worker_id')
    )
    op.create_index(op.f('ix_worker_first_name'), 'worker', ['first_name'], unique=False)
    op.create_index(op.f('ix_worker_last_name'), 'worker', ['last_name'], unique=False)
    op.create_index(op.f('ix_worker_phone_number'), 'worker', ['phone_number'], unique=True)
    op.create_index(op.f('ix_worker_worker_id'), 'worker', ['worker_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_worker_worker_id'), table_name='worker')
    op.drop_index(op.f('ix_worker_phone_number'), table_name='worker')
    op.drop_index(op.f('ix_worker_last_name'), table_name='worker')
    op.drop_index(op.f('ix_worker_first_name'), table_name='worker')
    op.drop_table('worker')
    # ### end Alembic commands ###
