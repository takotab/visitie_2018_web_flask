"""users table

Revision ID: b5641923bd3c
Revises: 
Create Date: 2018-10-27 11:36:26.518994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5641923bd3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('praktijk', sa.String(length=25), nullable=True),
    sa.Column('regio', sa.String(length=25), nullable=True),
    sa.Column('num_therapeuten', sa.Integer(), nullable=True),
    sa.Column('bezoekende_praktijk', sa.String(length=25), nullable=True),
    sa.Column('te_bezoeken_praktijk', sa.String(length=25), nullable=True),
    sa.Column('vorig_bezoekende_praktijk', sa.String(length=25), nullable=True),
    sa.Column('vorig_te_bezoeken_praktijk', sa.String(length=25), nullable=True),
    sa.Column('vorig_catagorie', sa.String(length=25), nullable=True),
    sa.Column('vorig_name_code', sa.String(length=25), nullable=True),
    sa.Column('vorig_color', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_bezoekende_praktijk'), 'user', ['bezoekende_praktijk'], unique=True)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    op.create_index(op.f('ix_user_praktijk'), 'user', ['praktijk'], unique=False)
    op.create_index(op.f('ix_user_regio'), 'user', ['regio'], unique=False)
    op.create_index(op.f('ix_user_te_bezoeken_praktijk'), 'user', ['te_bezoeken_praktijk'], unique=True)
    op.create_index(op.f('ix_user_vorig_bezoekende_praktijk'), 'user', ['vorig_bezoekende_praktijk'], unique=True)
    op.create_index(op.f('ix_user_vorig_catagorie'), 'user', ['vorig_catagorie'], unique=False)
    op.create_index(op.f('ix_user_vorig_color'), 'user', ['vorig_color'], unique=False)
    op.create_index(op.f('ix_user_vorig_name_code'), 'user', ['vorig_name_code'], unique=False)
    op.create_index(op.f('ix_user_vorig_te_bezoeken_praktijk'), 'user', ['vorig_te_bezoeken_praktijk'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_vorig_te_bezoeken_praktijk'), table_name='user')
    op.drop_index(op.f('ix_user_vorig_name_code'), table_name='user')
    op.drop_index(op.f('ix_user_vorig_color'), table_name='user')
    op.drop_index(op.f('ix_user_vorig_catagorie'), table_name='user')
    op.drop_index(op.f('ix_user_vorig_bezoekende_praktijk'), table_name='user')
    op.drop_index(op.f('ix_user_te_bezoeken_praktijk'), table_name='user')
    op.drop_index(op.f('ix_user_regio'), table_name='user')
    op.drop_index(op.f('ix_user_praktijk'), table_name='user')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_bezoekende_praktijk'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###