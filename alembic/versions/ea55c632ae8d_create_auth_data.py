"""Create auth data.

Revision ID: ea55c632ae8d
Revises: 0ff7fe2828a5
Create Date: 2016-05-06 11:09:58.943048

"""

# revision identifiers, used by Alembic.
revision = 'ea55c632ae8d'
down_revision = '0ff7fe2828a5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Upgrade the database to a newer revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=True),
                    sa.Column('description', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name'))
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('login', sa.String(length=255), nullable=True),
                    sa.Column('email', sa.String(length=255), nullable=True),
                    sa.Column('password', sa.String(length=255), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=True),
                    sa.Column('token', sa.String(length=255), nullable=True),
                    sa.Column('token_expires', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('login'))
    op.create_table('roles_users',
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ))
    # end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_users')
    op.drop_table('user')
    op.drop_table('role')
    # end Alembic commands ###
