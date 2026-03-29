"""initial schema: symptoms, synonyms, conditions, links, recommendations

Revision ID: 001_initial
Revises:
Create Date: 2026-03-28

"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "symptoms",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug", name="uq_symptoms_slug"),
    )
    op.create_index(op.f("ix_symptoms_slug"), "symptoms", ["slug"], unique=False)

    op.create_table(
        "conditions",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug", name="uq_conditions_slug"),
    )
    op.create_index(op.f("ix_conditions_slug"), "conditions", ["slug"], unique=False)

    op.create_table(
        "symptom_synonyms",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("symptom_id", sa.Integer(), nullable=False),
        sa.Column("text", sa.String(length=512), nullable=False),
        sa.ForeignKeyConstraint(["symptom_id"], ["symptoms.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_symptom_synonyms_text"), "symptom_synonyms", ["text"], unique=False)

    op.create_table(
        "condition_symptoms",
        sa.Column("condition_id", sa.Integer(), nullable=False),
        sa.Column("symptom_id", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Float(), server_default=sa.text("1.0"), nullable=False),
        sa.ForeignKeyConstraint(["condition_id"], ["conditions.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["symptom_id"], ["symptoms.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("condition_id", "symptom_id"),
    )

    op.create_table(
        "recommendations",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("condition_id", sa.Integer(), nullable=True),
        sa.Column("title", sa.String(length=512), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("category", sa.String(length=128), nullable=True),
        sa.ForeignKeyConstraint(["condition_id"], ["conditions.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_recommendations_condition_id"), "recommendations", ["condition_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_recommendations_condition_id"), table_name="recommendations")
    op.drop_table("recommendations")
    op.drop_table("condition_symptoms")
    op.drop_index(op.f("ix_symptom_synonyms_text"), table_name="symptom_synonyms")
    op.drop_table("symptom_synonyms")
    op.drop_index(op.f("ix_conditions_slug"), table_name="conditions")
    op.drop_table("conditions")
    op.drop_index(op.f("ix_symptoms_slug"), table_name="symptoms")
    op.drop_table("symptoms")
