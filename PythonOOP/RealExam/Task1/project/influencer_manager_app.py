from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type != "PremiumInfluencer" and influencer_type != "StandardInfluencer":
            return f"{influencer_type} is not an allowed influencer type."
        for influencer in self.influencers:
            if username == influencer.username:
                return f"{username} is already registered."

        if influencer_type == "PremiumInfluencer":
            influencer = PremiumInfluencer(username, followers, engagement_rate)
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."
        if influencer_type == "StandardInfluencer":
            influencer = StandardInfluencer(username, followers, engagement_rate)
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type != "HighBudgetCampaign" and campaign_type != "LowBudgetCampaign":
            return f"{campaign_type} is not a valid campaign type."

        for campaign in self.campaigns:
            if campaign_id == campaign.campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        if campaign_type == "HighBudgetCampaign":
            campaign = HighBudgetCampaign(campaign_id, brand, required_engagement)
            self.campaigns.append(campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

        if campaign_type == "LowBudgetCampaign":
            campaign = LowBudgetCampaign(campaign_id, brand, required_engagement)
            self.campaigns.append(campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        for influencer in self.influencers:
            if influencer.username == influencer_username:
                for campaign in self.campaigns:
                    if campaign_id == campaign.campaign_id:
                        if not campaign.check_eligibility(influencer.engagement_rate):
                            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."
                        if influencer.calculate_payment(campaign) > 0:
                            campaign.approved_influencers.append(influencer)
                            campaign.budget -= influencer.calculate_payment(campaign)
                            influencer.campaign_participated.append(campaign)
                            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."
                return f"Campaign with ID {campaign_id} not found."
        return f"Influencer '{influencer_username}' not found."

    def calculate_total_reached_followers(self):
        followers_in_campaigns = {}
        for campaign in self.campaigns:
            total_followers = 0
            if len(campaign.approved_influencers) > 0:
                for influencer in campaign.approved_influencers:
                    total_followers += influencer.reached_followers(campaign.__class__.__name__)

                followers_in_campaigns[campaign] = total_followers

        return followers_in_campaigns

    def influencer_campaign_report(self, username: str):
        for influencer in self.influencers:
            if influencer.username == username:
                if len(influencer.campaign_participated) == 0:
                    return f"{username} has not participated in any campaigns."
                return influencer.display_campaign_participated()

    def campaign_statistics(self):
        influencers_in_campaign = []
        for campaign in self.campaigns:
            total_influencers = len(campaign.approved_influencers)
            total_budget = campaign.budget
            total_reached_followers = 0
            for influencer in campaign.approved_influencers:
                total_reached_followers += influencer.reached_followers(campaign.__class__.__name__)
            #total_reached_followers = campaign.calculate_total_reached_followers()

            influencers_in_campaign.append((campaign, total_influencers, total_budget, total_reached_followers))

        sorted_campaigns = sorted(influencers_in_campaign, key=lambda x: (x[1], -x[2]))

        final = "$$ Campaign Statistics $$\n"
        for campaign, total_influencers, total_budget, total_reached_followers in sorted_campaigns:
            final += f"  * Brand: {campaign.brand}, Total influencers: {total_influencers}, Total budget: ${total_budget:.2f}, Total reached followers: {total_reached_followers}\n"

        return final
 