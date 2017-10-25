"""empty message

Revision ID: ecb863afa588
Revises: cdbe053b385f
Create Date: 2017-10-25 14:56:06.246610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecb863afa588'
down_revision = 'cdbe053b385f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shoppinglistitems',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('shoppinglist_id', sa.Integer(), nullable=False),
    sa.Column('item_title', sa.String(length=255), nullable=False),
    sa.Column('item_description', sa.String(length=500), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('item_id'),
    sa.UniqueConstraint('item_title')
    )
    op.create_unique_constraint(None, 'shoppinglists', ['title'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shoppinglists', type_='unique')
    op.drop_table('shoppinglistitems')
    # ### end Alembic commands ###