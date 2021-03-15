"""add status column

Revision ID: dce6faea1c20
Revises: 
Create Date: 2021-03-15 08:04:11.714082

"""
from alembic import op
import sqlalchemy as sa

import EnumAsInteger from enumtype
import Status from models


# revision identifiers, used by Alembic.
revision = 'dce6faea1c20'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('domains', sa.Column('status', EnumAsInteger(Status), nullable=True))
    

def downgrade():
    op.drop_column('domains', 'status')