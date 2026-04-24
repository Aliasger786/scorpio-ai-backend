"""Dashboard and authentication views for Aura AI."""
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def dashboard_stats(request):
    """Get dashboard statistics."""
    try:
        # Mock data for now - replace with real database queries
        stats = {
            'total_agents': 13,
            'active_users': 1247,
            'total_runs': 45832,
            'success_rate': 98.5,
            'business_usage': 67.3,
            'healthcare_usage': 32.7,
            'recent_activity': [
                {
                    'id': '1',
                    'type': 'agent_run',
                    'description': 'Lead Outreach Agent executed for 25 prospects',
                    'user_id': 'user-1',
                    'timestamp': '2024-01-15T16:45:00Z',
                    'metadata': {
                        'agent_id': '1',
                        'prospects_count': 25,
                        'success_rate': 92
                    }
                },
                {
                    'id': '2',
                    'type': 'agent_run',
                    'description': 'SOAP Note Draft Agent completed for patient visit',
                    'user_id': 'user-2',
                    'timestamp': '2024-01-15T16:30:00Z',
                    'metadata': {
                        'agent_id': '8',
                        'patient_id': 'patient-123',
                        'visit_type': 'follow-up'
                    }
                }
            ]
        }
        
        return JsonResponse(stats, status=status.HTTP_200_OK)
        
    except Exception as e:
        logger.error(f"Dashboard stats error: {str(e)}")
        return JsonResponse({
            'error': 'Failed to fetch dashboard statistics'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
