"""add last_visit to patients

Revision ID: add_last_visit_to_patients
Revises: create_patients_table
Create Date: 2024-03-19 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_last_visit_to_patients'
down_revision = 'create_patients_table'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('patients', sa.Column('last_visit', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))

def downgrade():
    op.drop_column('patients', 'last_visit') 