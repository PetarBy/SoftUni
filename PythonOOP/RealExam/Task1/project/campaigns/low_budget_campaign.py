from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    BUDGET = 2500
    ENGAGEMENT_CHECK = False
    #TYPE_OF_CAMPAIGN = "LowBudgetCampaign"

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, LowBudgetCampaign.BUDGET, required_engagement)
        #self.type_of_campaign = LowBudgetCampaign.TYPE_OF_CAMPAIGN

    def check_eligibility(self, engagement_rate: float):
        if engagement_rate >= 0.9 * self.required_engagement:
            LowBudgetCampaign.ENGAGEMENT_CHECK = True
            return LowBudgetCampaign.ENGAGEMENT_CHECK
        LowBudgetCampaign.ENGAGEMENT_CHECK = False
        return LowBudgetCampaign.ENGAGEMENT_CHECK
