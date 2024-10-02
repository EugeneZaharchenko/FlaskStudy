"""add film model

Revision ID: e71ddb7ac5fd
Revises: 
Create Date: 2024-09-20 09:08:01.743772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e71ddb7ac5fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('film',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('distributed_by', sa.String(length=128), nullable=False),
    sa.Column('length', sa.Float(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_film_release_date'), ['release_date'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_film_release_date'))

    op.drop_table('film')
    # ### end Alembic commands ###
