"""Changed pet attributes.

Revision ID: f737dd94684f
Revises: 5dd9d13500a5
Create Date: 2024-05-25 20:56:48.393680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f737dd94684f'
down_revision = '5dd9d13500a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pet', schema=None) as batch_op:
        batch_op.drop_column('gender')

    # ### end Alembic commands ###
