import allure
import pytest

from common.readyaml import get_testcase_yaml
from base.apiutil_logistics import LogisticsRequestBase #业务层请求工具
from base.generateId import m_id, c_id

@allure.feature(next(m_id) + '物流管理系统（业务场景）')
class TestLogisticsScenario:

    @allure.story(next(c_id) + '物流单创建-分配-签收全流程')
    @pytest.mark.parametrize('case_info', get_testcase_yaml('./testcase/LogisticsManager/LogisticsScenario.yml'))
    def test_logistics_full_process(self, case_info):
        allure.dynamic.title(case_info['baseInfo']['api_name'])
        LogisticsRequestBase().specification_yaml(case_info)

@allure.feature(next(m_id) + '物流管理系统（单接口）')
class TestLogisticsSingle:

    @allure.story(next(c_id) + '集团分配订单')
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml('./testcase/LogisticsManager/assignOrder.yaml'))
    def test_assign_order(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        case_info = {'baseInfo': base_info, 'testCase': [testcase]}
        LogisticsRequestBase().specification_yaml(case_info)

    @allure.story(next(c_id) + '司机确认运输')
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml('./testcase/LogisticsManager/driverConfirm.yaml'))
    def test_driver_confirm(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        case_info = {'baseInfo': base_info, 'testCase': [testcase]}
        LogisticsRequestBase().specification_yaml(case_info)

    @allure.story(next(c_id) + '获取调度单详情')
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml('./testcase/LogisticsManager/scheduleDetail.yaml'))
    def test_schedule_detail(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        case_info = {'baseInfo': base_info, 'testCase': [testcase]}
        LogisticsRequestBase().specification_yaml(case_info)

    @allure.story(next(c_id) + '物流公司拆分订单')
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml('./testcase/LogisticsManager/splitOrder.yaml'))
    def test_split_order(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        case_info = {'baseInfo': base_info, 'testCase': [testcase]}
        LogisticsRequestBase().specification_yaml(case_info)