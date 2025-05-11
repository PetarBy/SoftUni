from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    BUDGET = 5000
    ENGAGEMENT_CHECK = False
    #TYPE_OF_CAMPAIGN = "HighBudgetCampaign"

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, HighBudgetCampaign.BUDGET, required_engagement)
        #self.type_of_campaign = HighBudgetCampaign.TYPE_OF_CAMPAIGN

    def check_eligibility(self, engagement_rate: float):
        if engagement_rate >= 1.2 * self.required_engagement:
            HighBudgetCampaign.ENGAGEMENT_CHECK = True
            return HighBudgetCampaign.ENGAGEMENT_CHECK
        HighBudgetCampaign.ENGAGEMENT_CHECK = False
        return HighBudgetCampaign.ENGAGEMENT_CHECK


