"""empty message

Revision ID: 0f2b4cf90432
Revises: 
Create Date: 2024-12-17 17:46:42.434783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f2b4cf90432'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('admin_username', sa.String(length=100), nullable=False),
    sa.Column('admin_password', sa.String(length=200), nullable=False),
    sa.Column('admin_email', sa.String(length=255), nullable=False),
    sa.Column('admin_logindate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('admin_id'),
    sa.UniqueConstraint('admin_email')
    )
    op.create_table('category',
    sa.Column('cat_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cat_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('cat_id')
    )
    op.create_table('state',
    sa.Column('state_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('state_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('state_id')
    )
    op.create_table('worker',
    sa.Column('worker_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('worker_fname', sa.String(length=100), nullable=False),
    sa.Column('worker_lname', sa.String(length=100), nullable=False),
    sa.Column('worker_email', sa.String(length=255), nullable=False),
    sa.Column('worker_phoneno', sa.String(length=100), nullable=False),
    sa.Column('worker_password', sa.String(length=200), nullable=False),
    sa.Column('worker_status', sa.Enum('0', '1'), server_default='0', nullable=False),
    sa.Column('worker_registrationdate', sa.DateTime(), nullable=True),
    sa.Column('worker_gender', sa.String(length=45), nullable=False),
    sa.Column('worker_picture', sa.LargeBinary(), nullable=False),
    sa.Column('worker_availability', sa.Enum('0', '1'), server_default='0', nullable=False),
    sa.Column('worker_verification', sa.Enum('0', '1'), server_default='0', nullable=False),
    sa.PrimaryKeyConstraint('worker_id'),
    sa.UniqueConstraint('worker_email')
    )
    op.create_table('employer',
    sa.Column('employer_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('employer_name', sa.String(length=100), nullable=False),
    sa.Column('employer_email', sa.String(length=255), nullable=False),
    sa.Column('employer_password', sa.String(length=200), nullable=False),
    sa.Column('employer_address', sa.Text(), nullable=True),
    sa.Column('employer_gender', sa.String(length=45), nullable=True),
    sa.Column('employer_picture', sa.LargeBinary(), nullable=True),
    sa.Column('employer_phoneno', sa.String(length=100), nullable=True),
    sa.Column('date_registered', sa.DateTime(), nullable=True),
    sa.Column('employer_stateid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employer_stateid'], ['state.state_id'], ),
    sa.PrimaryKeyConstraint('employer_id'),
    sa.UniqueConstraint('employer_email')
    )
    op.create_table('experience',
    sa.Column('exp_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('exp_jobtitle', sa.String(length=50), nullable=False),
    sa.Column('exp_startdate', sa.DateTime(), nullable=False),
    sa.Column('exp_enddate', sa.DateTime(), nullable=False),
    sa.Column('exp_workerid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['exp_workerid'], ['worker.worker_id'], ),
    sa.PrimaryKeyConstraint('exp_id')
    )
    op.create_table('jobapplication',
    sa.Column('app_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('app_status', sa.Enum('0', '1'), server_default='0', nullable=False),
    sa.Column('app_dateapplied', sa.DateTime(), nullable=True),
    sa.Column('app_agreedamount', sa.Numeric(), nullable=False),
    sa.Column('app_workerid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['app_workerid'], ['worker.worker_id'], ),
    sa.PrimaryKeyConstraint('app_id')
    )
    op.create_table('jobposting',
    sa.Column('post_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post_title', sa.String(length=100), nullable=False),
    sa.Column('post_description', sa.Text(), nullable=False),
    sa.Column('post_payrate', sa.Numeric(), nullable=False),
    sa.Column('post_dateadded', sa.DateTime(), nullable=False),
    sa.Column('post_closingdate', sa.DateTime(), nullable=False),
    sa.Column('post_status', sa.Enum('0', '1'), server_default='0', nullable=False),
    sa.Column('post_categoryid', sa.Integer(), nullable=True),
    sa.Column('post_employerid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_categoryid'], ['category.cat_id'], ),
    sa.ForeignKeyConstraint(['post_employerid'], ['employer.employer_id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_table('payment',
    sa.Column('pay_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pay_amount', sa.Numeric(), nullable=False),
    sa.Column('pay_date', sa.DateTime(), nullable=False),
    sa.Column('pay_status', sa.Enum('0', '1'), server_default='0', nullable=False),
    sa.Column('pay_employerid', sa.Integer(), nullable=True),
    sa.Column('pay_appid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pay_appid'], ['worker.worker_id'], ),
    sa.ForeignKeyConstraint(['pay_employerid'], ['employer.employer_id'], ),
    sa.PrimaryKeyConstraint('pay_id')
    )
    op.create_table('review',
    sa.Column('review_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('review_rating', sa.Float(), nullable=False),
    sa.Column('review_comment', sa.Text(), nullable=False),
    sa.Column('review_workerid', sa.Integer(), nullable=True),
    sa.Column('review_employerid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['review_employerid'], ['employer.employer_id'], ),
    sa.ForeignKeyConstraint(['review_workerid'], ['worker.worker_id'], ),
    sa.PrimaryKeyConstraint('review_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('payment')
    op.drop_table('jobposting')
    op.drop_table('jobapplication')
    op.drop_table('experience')
    op.drop_table('employer')
    op.drop_table('worker')
    op.drop_table('state')
    op.drop_table('category')
    op.drop_table('admin')
    # ### end Alembic commands ###