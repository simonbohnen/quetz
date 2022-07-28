"""tos_languages

Revision ID: c3a635971280
Revises: 44ec522465e5
Create Date: 2022-07-27 15:15:22.341630

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c3a635971280'
down_revision = '44ec522465e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'quetz_tos_file',
        sa.Column('id', sa.LargeBinary(length=16), nullable=False),
        sa.Column('filename', sa.String(), nullable=True),
        sa.Column('language', sa.String(), nullable=True),
        sa.Column('tos_id', sa.LargeBinary(length=16), nullable=False),
        sa.ForeignKeyConstraint(
            ['tos_id'],
            ['quetz_tos.id'],
        ),
        sa.PrimaryKeyConstraint('id', 'tos_id'),
    )
    with op.batch_alter_table('channels', schema=None) as batch_op:
        batch_op.alter_column(
            'size',
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )
        batch_op.alter_column(
            'size_limit',
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )

    with op.batch_alter_table('package_versions', schema=None) as batch_op:
        batch_op.alter_column(
            'size',
            existing_type=sa.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=True,
        )

    with op.batch_alter_table('quetz_tos', schema=None) as batch_op:
        batch_op.drop_column('filename')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quetz_tos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('filename', sa.VARCHAR(), nullable=True))

    with op.batch_alter_table('package_versions', schema=None) as batch_op:
        batch_op.alter_column(
            'size',
            existing_type=sa.BigInteger(),
            type_=sa.INTEGER(),
            existing_nullable=True,
        )

    with op.batch_alter_table('channels', schema=None) as batch_op:
        batch_op.alter_column(
            'size_limit',
            existing_type=sa.BigInteger(),
            type_=sa.INTEGER(),
            existing_nullable=True,
        )
        batch_op.alter_column(
            'size',
            existing_type=sa.BigInteger(),
            type_=sa.INTEGER(),
            existing_nullable=True,
        )

    op.drop_table('quetz_tos_file')
    # ### end Alembic commands ###
