"""empty message

Revision ID: 881adb1b3ee7
Revises: e82fb205239c
Create Date: 2020-03-25 10:44:10.237796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '881adb1b3ee7'
down_revision = 'e82fb205239c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_upload',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_my_upload_created_on'), 'my_upload', ['created_on'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_my_upload_created_on'), table_name='my_upload')
    op.drop_table('my_upload')
    # ### end Alembic commands ###
