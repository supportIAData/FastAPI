"""Create cases table

Revision ID: 25b9b77923ee
Revises: 
Create Date: 2023-05-10 15:37:27.884341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25b9b77923ee'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
      'cases',
      sa.Column("id", sa.Integer, primary_key=True),
      sa.Column("name", sa.String(200)),
      sa.Column("active", sa.Boolean),
    )


def downgrade() -> None:
    op.drop_table('cases')
