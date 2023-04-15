"""rename sent column

Revision ID: ae98339276a4
Revises: 80a4b5684683
Create Date: 2023-04-15 05:44:29.353001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae98339276a4'
down_revision = '80a4b5684683'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('is_sent', sa.Boolean(), server_default=sa.text('0'), nullable=False))
    op.drop_column('jobs', 'sent')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('sent', sa.BOOLEAN(), server_default=sa.text('0'), nullable=False))
    op.drop_column('jobs', 'is_sent')
    # ### end Alembic commands ###
