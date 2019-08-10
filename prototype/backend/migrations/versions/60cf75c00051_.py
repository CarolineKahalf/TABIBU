"""empty message

Revision ID: 60cf75c00051
Revises: 
Create Date: 2019-07-17 17:25:29.314548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60cf75c00051'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('public_id', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('date_registered', sa.DateTime(), nullable=False),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('public_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('image_path'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('doctor',
    sa.Column('doctor_id', sa.String(), nullable=True),
    sa.Column('public_id', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('date_registered', sa.DateTime(), nullable=False),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('cert_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('public_id'),
    sa.UniqueConstraint('cert_path'),
    sa.UniqueConstraint('doctor_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('image_path'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('patient',
    sa.Column('public_id', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('date_registered', sa.DateTime(), nullable=False),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('public_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('image_path'),
    sa.UniqueConstraint('public_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patient')
    op.drop_table('doctor')
    op.drop_table('blacklist_tokens')
    op.drop_table('admin')
    # ### end Alembic commands ###
