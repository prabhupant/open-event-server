"""empty message

Revision ID: 7ed42c8dc5cc
Revises: 460a04b3e98e
Create Date: 2016-06-03 03:30:19.507259

"""

# revision identifiers, used by Alembic.
revision = '7ed42c8dc5cc'
down_revision = '460a04b3e98e'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('background_url', sa.String(), nullable=True))
    op.add_column('events', sa.Column('event_url', sa.String(), nullable=True))
    op.drop_column('events', 'url')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('events', 'event_url')
    op.drop_column('events', 'background_url')
    ### end Alembic commands ###