"""add chats table and restructure user table

Revision ID: 4da267e5129f
Revises: 293338a97664
Create Date: 2025-03-01 15:04:30.950331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4da267e5129f'
down_revision = '293338a97664'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
        batch_op.drop_constraint('users_username_key', type_='unique')
        batch_op.drop_column('chat_memory')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('chat_memory', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.create_unique_constraint('users_username_key', ['username'])
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
