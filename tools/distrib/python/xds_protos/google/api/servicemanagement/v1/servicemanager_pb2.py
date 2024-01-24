# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/servicemanagement/v1/servicemanager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import service_pb2 as google_dot_api_dot_service__pb2
from google.api.servicemanagement.v1 import resources_pb2 as google_dot_api_dot_servicemanagement_dot_v1_dot_resources__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/api/servicemanagement/v1/servicemanager.proto\x12\x1fgoogle.api.servicemanagement.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x18google/api/service.proto\x1a/google/api/servicemanagement/v1/resources.proto\x1a#google/longrunning/operations.proto\x1a\x19google/protobuf/any.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"r\n\x13ListServicesRequest\x12\x1b\n\x13producer_project_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\x12\x17\n\x0b\x63onsumer_id\x18\x07 \x01(\tB\x02\x18\x01\"r\n\x14ListServicesResponse\x12\x41\n\x08services\x18\x01 \x03(\x0b\x32/.google.api.servicemanagement.v1.ManagedService\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"/\n\x11GetServiceRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"^\n\x14\x43reateServiceRequest\x12\x46\n\x07service\x18\x01 \x01(\x0b\x32/.google.api.servicemanagement.v1.ManagedServiceB\x04\xe2\x41\x01\x02\"2\n\x14\x44\x65leteServiceRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"4\n\x16UndeleteServiceRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"[\n\x17UndeleteServiceResponse\x12@\n\x07service\x18\x01 \x01(\x0b\x32/.google.api.servicemanagement.v1.ManagedService\"\xc4\x01\n\x17GetServiceConfigRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x17\n\tconfig_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02\x12Q\n\x04view\x18\x03 \x01(\x0e\x32\x43.google.api.servicemanagement.v1.GetServiceConfigRequest.ConfigView\"!\n\nConfigView\x12\t\n\x05\x42\x41SIC\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\"^\n\x19ListServiceConfigsRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\"c\n\x1aListServiceConfigsResponse\x12,\n\x0fservice_configs\x18\x01 \x03(\x0b\x32\x13.google.api.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"k\n\x1a\x43reateServiceConfigRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x31\n\x0eservice_config\x18\x02 \x01(\x0b\x32\x13.google.api.ServiceB\x04\xe2\x41\x01\x02\"\xa0\x01\n\x19SubmitConfigSourceRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12J\n\rconfig_source\x18\x02 \x01(\x0b\x32-.google.api.servicemanagement.v1.ConfigSourceB\x04\xe2\x41\x01\x02\x12\x1b\n\rvalidate_only\x18\x03 \x01(\x08\x42\x04\xe2\x41\x01\x01\"I\n\x1aSubmitConfigSourceResponse\x12+\n\x0eservice_config\x18\x01 \x01(\x0b\x32\x13.google.api.Service\"z\n\x1b\x43reateServiceRolloutRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12?\n\x07rollout\x18\x02 \x01(\x0b\x32(.google.api.servicemanagement.v1.RolloutB\x04\xe2\x41\x01\x02\"u\n\x1aListServiceRolloutsRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x14\n\x06\x66ilter\x18\x04 \x01(\tB\x04\xe2\x41\x01\x02\"r\n\x1bListServiceRolloutsResponse\x12:\n\x08rollouts\x18\x01 \x03(\x0b\x32(.google.api.servicemanagement.v1.Rollout\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"P\n\x18GetServiceRolloutRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x18\n\nrollout_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02\"M\n\x14\x45nableServiceRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x19\n\x0b\x63onsumer_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02\"\x17\n\x15\x45nableServiceResponse\"N\n\x15\x44isableServiceRequest\x12\x1a\n\x0cservice_name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x19\n\x0b\x63onsumer_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02\"\x18\n\x16\x44isableServiceResponse\"}\n\x1bGenerateConfigReportRequest\x12.\n\nnew_config\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x04\xe2\x41\x01\x02\x12.\n\nold_config\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x04\xe2\x41\x01\x01\"\xc9\x01\n\x1cGenerateConfigReportResponse\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x45\n\x0e\x63hange_reports\x18\x03 \x03(\x0b\x32-.google.api.servicemanagement.v1.ChangeReport\x12@\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32+.google.api.servicemanagement.v1.Diagnostic2\x92\x1e\n\x0eServiceManager\x12\xb3\x01\n\x0cListServices\x12\x34.google.api.servicemanagement.v1.ListServicesRequest\x1a\x35.google.api.servicemanagement.v1.ListServicesResponse\"6\xda\x41\x1fproducer_project_id,consumer_id\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/services\x12\xa5\x01\n\nGetService\x12\x32.google.api.servicemanagement.v1.GetServiceRequest\x1a/.google.api.servicemanagement.v1.ManagedService\"2\xda\x41\x0cservice_name\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/services/{service_name}\x12\xf5\x01\n\rCreateService\x12\x35.google.api.servicemanagement.v1.CreateServiceRequest\x1a\x1d.google.longrunning.Operation\"\x8d\x01\xca\x41\x63\n.google.api.servicemanagement.v1.ManagedService\x12\x31google.api.servicemanagement.v1.OperationMetadata\xda\x41\x07service\x82\xd3\xe4\x93\x02\x17\"\x0c/v1/services:\x07service\x12\xe6\x01\n\rDeleteService\x12\x35.google.api.servicemanagement.v1.DeleteServiceRequest\x1a\x1d.google.longrunning.Operation\"\x7f\xca\x41J\n\x15google.protobuf.Empty\x12\x31google.api.servicemanagement.v1.OperationMetadata\xda\x41\x0cservice_name\x82\xd3\xe4\x93\x02\x1d*\x1b/v1/services/{service_name}\x12\x96\x02\n\x0fUndeleteService\x12\x37.google.api.servicemanagement.v1.UndeleteServiceRequest\x1a\x1d.google.longrunning.Operation\"\xaa\x01\xca\x41l\n7google.api.servicemanagement.v1.UndeleteServiceResponse\x12\x31google.api.servicemanagement.v1.OperationMetadata\xda\x41\x0cservice_name\x82\xd3\xe4\x93\x02&\"$/v1/services/{service_name}:undelete\x12\xc9\x01\n\x12ListServiceConfigs\x12:.google.api.servicemanagement.v1.ListServiceConfigsRequest\x1a;.google.api.servicemanagement.v1.ListServiceConfigsResponse\":\xda\x41\x0cservice_name\x82\xd3\xe4\x93\x02%\x12#/v1/services/{service_name}/configs\x12\xde\x01\n\x10GetServiceConfig\x12\x38.google.api.servicemanagement.v1.GetServiceConfigRequest\x1a\x13.google.api.Service\"{\xda\x41\x1bservice_name,config_id,view\x82\xd3\xe4\x93\x02W\x12//v1/services/{service_name}/configs/{config_id}Z$\x12\"/v1/services/{service_name}/config\x12\xc2\x01\n\x13\x43reateServiceConfig\x12;.google.api.servicemanagement.v1.CreateServiceConfigRequest\x1a\x13.google.api.Service\"Y\xda\x41\x1bservice_name,service_config\x82\xd3\xe4\x93\x02\x35\"#/v1/services/{service_name}/configs:\x0eservice_config\x12\xc4\x02\n\x12SubmitConfigSource\x12:.google.api.servicemanagement.v1.SubmitConfigSourceRequest\x1a\x1d.google.longrunning.Operation\"\xd2\x01\xca\x41o\n:google.api.servicemanagement.v1.SubmitConfigSourceResponse\x12\x31google.api.servicemanagement.v1.OperationMetadata\xda\x41(service_name,config_source,validate_only\x82\xd3\xe4\x93\x02/\"*/v1/services/{service_name}/configs:submit:\x01*\x12\xd4\x01\n\x13ListServiceRollouts\x12;.google.api.servicemanagement.v1.ListServiceRolloutsRequest\x1a<.google.api.servicemanagement.v1.ListServiceRolloutsResponse\"B\xda\x41\x13service_name,filter\x82\xd3\xe4\x93\x02&\x12$/v1/services/{service_name}/rollouts\x12\xcd\x01\n\x11GetServiceRollout\x12\x39.google.api.servicemanagement.v1.GetServiceRolloutRequest\x1a(.google.api.servicemanagement.v1.Rollout\"S\xda\x41\x17service_name,rollout_id\x82\xd3\xe4\x93\x02\x33\x12\x31/v1/services/{service_name}/rollouts/{rollout_id}\x12\xa1\x02\n\x14\x43reateServiceRollout\x12<.google.api.servicemanagement.v1.CreateServiceRolloutRequest\x1a\x1d.google.longrunning.Operation\"\xab\x01\xca\x41\\\n\'google.api.servicemanagement.v1.Rollout\x12\x31google.api.servicemanagement.v1.OperationMetadata\xda\x41\x14service_name,rollout\x82\xd3\xe4\x93\x02/\"$/v1/services/{service_name}/rollouts:\x07rollout\x12\xd9\x01\n\x14GenerateConfigReport\x12<.google.api.servicemanagement.v1.GenerateConfigReportRequest\x1a=.google.api.servicemanagement.v1.GenerateConfigReportResponse\"D\xda\x41\x15new_config,old_config\x82\xd3\xe4\x93\x02&\"!/v1/services:generateConfigReport:\x01*\x12\xa0\x02\n\rEnableService\x12\x35.google.api.servicemanagement.v1.EnableServiceRequest\x1a\x1d.google.longrunning.Operation\"\xb8\x01\x88\x02\x01\xca\x41j\n5google.api.servicemanagement.v1.EnableServiceResponse\x12\x31google.api.servicemanagement.v1.OperationMetadata\xda\x41\x18service_name,consumer_id\x82\xd3\xe4\x93\x02\'\"\"/v1/services/{service_name}:enable:\x01*\x12\xa4\x02\n\x0e\x44isableService\x12\x36.google.api.servicemanagement.v1.DisableServiceRequest\x1a\x1d.google.longrunning.Operation\"\xba\x01\x88\x02\x01\xca\x41k\n6google.api.servicemanagement.v1.DisableServiceResponse\x12\x31google.api.servicemanagement.v1.OperationMetadata\xda\x41\x18service_name,consumer_id\x82\xd3\xe4\x93\x02(\"#/v1/services/{service_name}:disable:\x01*\x1a\xfd\x01\xca\x41 servicemanagement.googleapis.com\xd2\x41\xd6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/service.management,https://www.googleapis.com/auth/service.management.readonlyB\x84\x02\n#com.google.api.servicemanagement.v1B\x13ServiceManagerProtoP\x01ZPgoogle.golang.org/genproto/googleapis/api/servicemanagement/v1;servicemanagement\xa2\x02\x04GASM\xaa\x02!Google.Cloud.ServiceManagement.V1\xca\x02!Google\\Cloud\\ServiceManagement\\V1\xea\x02$Google::Cloud::ServiceManagement::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.servicemanagement.v1.servicemanager_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.api.servicemanagement.v1B\023ServiceManagerProtoP\001ZPgoogle.golang.org/genproto/googleapis/api/servicemanagement/v1;servicemanagement\242\002\004GASM\252\002!Google.Cloud.ServiceManagement.V1\312\002!Google\\Cloud\\ServiceManagement\\V1\352\002$Google::Cloud::ServiceManagement::V1'
  _LISTSERVICESREQUEST.fields_by_name['consumer_id']._options = None
  _LISTSERVICESREQUEST.fields_by_name['consumer_id']._serialized_options = b'\030\001'
  _GETSERVICEREQUEST.fields_by_name['service_name']._options = None
  _GETSERVICEREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _CREATESERVICEREQUEST.fields_by_name['service']._options = None
  _CREATESERVICEREQUEST.fields_by_name['service']._serialized_options = b'\342A\001\002'
  _DELETESERVICEREQUEST.fields_by_name['service_name']._options = None
  _DELETESERVICEREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _UNDELETESERVICEREQUEST.fields_by_name['service_name']._options = None
  _UNDELETESERVICEREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _GETSERVICECONFIGREQUEST.fields_by_name['service_name']._options = None
  _GETSERVICECONFIGREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _GETSERVICECONFIGREQUEST.fields_by_name['config_id']._options = None
  _GETSERVICECONFIGREQUEST.fields_by_name['config_id']._serialized_options = b'\342A\001\002'
  _LISTSERVICECONFIGSREQUEST.fields_by_name['service_name']._options = None
  _LISTSERVICECONFIGSREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _CREATESERVICECONFIGREQUEST.fields_by_name['service_name']._options = None
  _CREATESERVICECONFIGREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _CREATESERVICECONFIGREQUEST.fields_by_name['service_config']._options = None
  _CREATESERVICECONFIGREQUEST.fields_by_name['service_config']._serialized_options = b'\342A\001\002'
  _SUBMITCONFIGSOURCEREQUEST.fields_by_name['service_name']._options = None
  _SUBMITCONFIGSOURCEREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _SUBMITCONFIGSOURCEREQUEST.fields_by_name['config_source']._options = None
  _SUBMITCONFIGSOURCEREQUEST.fields_by_name['config_source']._serialized_options = b'\342A\001\002'
  _SUBMITCONFIGSOURCEREQUEST.fields_by_name['validate_only']._options = None
  _SUBMITCONFIGSOURCEREQUEST.fields_by_name['validate_only']._serialized_options = b'\342A\001\001'
  _CREATESERVICEROLLOUTREQUEST.fields_by_name['service_name']._options = None
  _CREATESERVICEROLLOUTREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _CREATESERVICEROLLOUTREQUEST.fields_by_name['rollout']._options = None
  _CREATESERVICEROLLOUTREQUEST.fields_by_name['rollout']._serialized_options = b'\342A\001\002'
  _LISTSERVICEROLLOUTSREQUEST.fields_by_name['service_name']._options = None
  _LISTSERVICEROLLOUTSREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _LISTSERVICEROLLOUTSREQUEST.fields_by_name['filter']._options = None
  _LISTSERVICEROLLOUTSREQUEST.fields_by_name['filter']._serialized_options = b'\342A\001\002'
  _GETSERVICEROLLOUTREQUEST.fields_by_name['service_name']._options = None
  _GETSERVICEROLLOUTREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _GETSERVICEROLLOUTREQUEST.fields_by_name['rollout_id']._options = None
  _GETSERVICEROLLOUTREQUEST.fields_by_name['rollout_id']._serialized_options = b'\342A\001\002'
  _ENABLESERVICEREQUEST.fields_by_name['service_name']._options = None
  _ENABLESERVICEREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _ENABLESERVICEREQUEST.fields_by_name['consumer_id']._options = None
  _ENABLESERVICEREQUEST.fields_by_name['consumer_id']._serialized_options = b'\342A\001\002'
  _DISABLESERVICEREQUEST.fields_by_name['service_name']._options = None
  _DISABLESERVICEREQUEST.fields_by_name['service_name']._serialized_options = b'\342A\001\002'
  _DISABLESERVICEREQUEST.fields_by_name['consumer_id']._options = None
  _DISABLESERVICEREQUEST.fields_by_name['consumer_id']._serialized_options = b'\342A\001\002'
  _GENERATECONFIGREPORTREQUEST.fields_by_name['new_config']._options = None
  _GENERATECONFIGREPORTREQUEST.fields_by_name['new_config']._serialized_options = b'\342A\001\002'
  _GENERATECONFIGREPORTREQUEST.fields_by_name['old_config']._options = None
  _GENERATECONFIGREPORTREQUEST.fields_by_name['old_config']._serialized_options = b'\342A\001\001'
  _SERVICEMANAGER._options = None
  _SERVICEMANAGER._serialized_options = b'\312A servicemanagement.googleapis.com\322A\326\001https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/service.management,https://www.googleapis.com/auth/service.management.readonly'
  _SERVICEMANAGER.methods_by_name['ListServices']._options = None
  _SERVICEMANAGER.methods_by_name['ListServices']._serialized_options = b'\332A\037producer_project_id,consumer_id\202\323\344\223\002\016\022\014/v1/services'
  _SERVICEMANAGER.methods_by_name['GetService']._options = None
  _SERVICEMANAGER.methods_by_name['GetService']._serialized_options = b'\332A\014service_name\202\323\344\223\002\035\022\033/v1/services/{service_name}'
  _SERVICEMANAGER.methods_by_name['CreateService']._options = None
  _SERVICEMANAGER.methods_by_name['CreateService']._serialized_options = b'\312Ac\n.google.api.servicemanagement.v1.ManagedService\0221google.api.servicemanagement.v1.OperationMetadata\332A\007service\202\323\344\223\002\027\"\014/v1/services:\007service'
  _SERVICEMANAGER.methods_by_name['DeleteService']._options = None
  _SERVICEMANAGER.methods_by_name['DeleteService']._serialized_options = b'\312AJ\n\025google.protobuf.Empty\0221google.api.servicemanagement.v1.OperationMetadata\332A\014service_name\202\323\344\223\002\035*\033/v1/services/{service_name}'
  _SERVICEMANAGER.methods_by_name['UndeleteService']._options = None
  _SERVICEMANAGER.methods_by_name['UndeleteService']._serialized_options = b'\312Al\n7google.api.servicemanagement.v1.UndeleteServiceResponse\0221google.api.servicemanagement.v1.OperationMetadata\332A\014service_name\202\323\344\223\002&\"$/v1/services/{service_name}:undelete'
  _SERVICEMANAGER.methods_by_name['ListServiceConfigs']._options = None
  _SERVICEMANAGER.methods_by_name['ListServiceConfigs']._serialized_options = b'\332A\014service_name\202\323\344\223\002%\022#/v1/services/{service_name}/configs'
  _SERVICEMANAGER.methods_by_name['GetServiceConfig']._options = None
  _SERVICEMANAGER.methods_by_name['GetServiceConfig']._serialized_options = b'\332A\033service_name,config_id,view\202\323\344\223\002W\022//v1/services/{service_name}/configs/{config_id}Z$\022\"/v1/services/{service_name}/config'
  _SERVICEMANAGER.methods_by_name['CreateServiceConfig']._options = None
  _SERVICEMANAGER.methods_by_name['CreateServiceConfig']._serialized_options = b'\332A\033service_name,service_config\202\323\344\223\0025\"#/v1/services/{service_name}/configs:\016service_config'
  _SERVICEMANAGER.methods_by_name['SubmitConfigSource']._options = None
  _SERVICEMANAGER.methods_by_name['SubmitConfigSource']._serialized_options = b'\312Ao\n:google.api.servicemanagement.v1.SubmitConfigSourceResponse\0221google.api.servicemanagement.v1.OperationMetadata\332A(service_name,config_source,validate_only\202\323\344\223\002/\"*/v1/services/{service_name}/configs:submit:\001*'
  _SERVICEMANAGER.methods_by_name['ListServiceRollouts']._options = None
  _SERVICEMANAGER.methods_by_name['ListServiceRollouts']._serialized_options = b'\332A\023service_name,filter\202\323\344\223\002&\022$/v1/services/{service_name}/rollouts'
  _SERVICEMANAGER.methods_by_name['GetServiceRollout']._options = None
  _SERVICEMANAGER.methods_by_name['GetServiceRollout']._serialized_options = b'\332A\027service_name,rollout_id\202\323\344\223\0023\0221/v1/services/{service_name}/rollouts/{rollout_id}'
  _SERVICEMANAGER.methods_by_name['CreateServiceRollout']._options = None
  _SERVICEMANAGER.methods_by_name['CreateServiceRollout']._serialized_options = b'\312A\\\n\'google.api.servicemanagement.v1.Rollout\0221google.api.servicemanagement.v1.OperationMetadata\332A\024service_name,rollout\202\323\344\223\002/\"$/v1/services/{service_name}/rollouts:\007rollout'
  _SERVICEMANAGER.methods_by_name['GenerateConfigReport']._options = None
  _SERVICEMANAGER.methods_by_name['GenerateConfigReport']._serialized_options = b'\332A\025new_config,old_config\202\323\344\223\002&\"!/v1/services:generateConfigReport:\001*'
  _SERVICEMANAGER.methods_by_name['EnableService']._options = None
  _SERVICEMANAGER.methods_by_name['EnableService']._serialized_options = b'\210\002\001\312Aj\n5google.api.servicemanagement.v1.EnableServiceResponse\0221google.api.servicemanagement.v1.OperationMetadata\332A\030service_name,consumer_id\202\323\344\223\002\'\"\"/v1/services/{service_name}:enable:\001*'
  _SERVICEMANAGER.methods_by_name['DisableService']._options = None
  _SERVICEMANAGER.methods_by_name['DisableService']._serialized_options = b'\210\002\001\312Ak\n6google.api.servicemanagement.v1.DisableServiceResponse\0221google.api.servicemanagement.v1.OperationMetadata\332A\030service_name,consumer_id\202\323\344\223\002(\"#/v1/services/{service_name}:disable:\001*'
  _globals['_LISTSERVICESREQUEST']._serialized_start=375
  _globals['_LISTSERVICESREQUEST']._serialized_end=489
  _globals['_LISTSERVICESRESPONSE']._serialized_start=491
  _globals['_LISTSERVICESRESPONSE']._serialized_end=605
  _globals['_GETSERVICEREQUEST']._serialized_start=607
  _globals['_GETSERVICEREQUEST']._serialized_end=654
  _globals['_CREATESERVICEREQUEST']._serialized_start=656
  _globals['_CREATESERVICEREQUEST']._serialized_end=750
  _globals['_DELETESERVICEREQUEST']._serialized_start=752
  _globals['_DELETESERVICEREQUEST']._serialized_end=802
  _globals['_UNDELETESERVICEREQUEST']._serialized_start=804
  _globals['_UNDELETESERVICEREQUEST']._serialized_end=856
  _globals['_UNDELETESERVICERESPONSE']._serialized_start=858
  _globals['_UNDELETESERVICERESPONSE']._serialized_end=949
  _globals['_GETSERVICECONFIGREQUEST']._serialized_start=952
  _globals['_GETSERVICECONFIGREQUEST']._serialized_end=1148
  _globals['_GETSERVICECONFIGREQUEST_CONFIGVIEW']._serialized_start=1115
  _globals['_GETSERVICECONFIGREQUEST_CONFIGVIEW']._serialized_end=1148
  _globals['_LISTSERVICECONFIGSREQUEST']._serialized_start=1150
  _globals['_LISTSERVICECONFIGSREQUEST']._serialized_end=1244
  _globals['_LISTSERVICECONFIGSRESPONSE']._serialized_start=1246
  _globals['_LISTSERVICECONFIGSRESPONSE']._serialized_end=1345
  _globals['_CREATESERVICECONFIGREQUEST']._serialized_start=1347
  _globals['_CREATESERVICECONFIGREQUEST']._serialized_end=1454
  _globals['_SUBMITCONFIGSOURCEREQUEST']._serialized_start=1457
  _globals['_SUBMITCONFIGSOURCEREQUEST']._serialized_end=1617
  _globals['_SUBMITCONFIGSOURCERESPONSE']._serialized_start=1619
  _globals['_SUBMITCONFIGSOURCERESPONSE']._serialized_end=1692
  _globals['_CREATESERVICEROLLOUTREQUEST']._serialized_start=1694
  _globals['_CREATESERVICEROLLOUTREQUEST']._serialized_end=1816
  _globals['_LISTSERVICEROLLOUTSREQUEST']._serialized_start=1818
  _globals['_LISTSERVICEROLLOUTSREQUEST']._serialized_end=1935
  _globals['_LISTSERVICEROLLOUTSRESPONSE']._serialized_start=1937
  _globals['_LISTSERVICEROLLOUTSRESPONSE']._serialized_end=2051
  _globals['_GETSERVICEROLLOUTREQUEST']._serialized_start=2053
  _globals['_GETSERVICEROLLOUTREQUEST']._serialized_end=2133
  _globals['_ENABLESERVICEREQUEST']._serialized_start=2135
  _globals['_ENABLESERVICEREQUEST']._serialized_end=2212
  _globals['_ENABLESERVICERESPONSE']._serialized_start=2214
  _globals['_ENABLESERVICERESPONSE']._serialized_end=2237
  _globals['_DISABLESERVICEREQUEST']._serialized_start=2239
  _globals['_DISABLESERVICEREQUEST']._serialized_end=2317
  _globals['_DISABLESERVICERESPONSE']._serialized_start=2319
  _globals['_DISABLESERVICERESPONSE']._serialized_end=2343
  _globals['_GENERATECONFIGREPORTREQUEST']._serialized_start=2345
  _globals['_GENERATECONFIGREPORTREQUEST']._serialized_end=2470
  _globals['_GENERATECONFIGREPORTRESPONSE']._serialized_start=2473
  _globals['_GENERATECONFIGREPORTRESPONSE']._serialized_end=2674
  _globals['_SERVICEMANAGER']._serialized_start=2677
  _globals['_SERVICEMANAGER']._serialized_end=6535
# @@protoc_insertion_point(module_scope)