from rest_framework.routers import DefaultRouter
from student.views import ParentViewSet, StudentViewSet

router = DefaultRouter()

router.register('parents', ParentViewSet, basename='parent')
router.register('student', StudentViewSet, basename='students')

urlpatterns = router.urls 
