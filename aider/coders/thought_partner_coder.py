from .thought_partner_prompts import ThoughtPartnerPrompts
from .base_coder import Coder


class ThoughtPartnerCoder(Coder):
    """Ask questions about code without making any changes."""

    edit_format = "thought-partner"
    gpt_prompts = ThoughtPartnerPrompts()
