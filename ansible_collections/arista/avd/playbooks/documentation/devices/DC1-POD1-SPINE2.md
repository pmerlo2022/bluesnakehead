# DC1-POD1-SPINE2
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)
- [EOS CLI](#eos-cli)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 10.6.1.11/24 | 10.6.1.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | mgmt | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf mgmt
   ip address 10.6.1.11/24
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---- | ----- |
| False | True |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgmt | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf mgmt
      no shutdown
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$82gqIqw8b3nibNrk$MoZO0S8QMQN8uwnR8v48dbGrL0Ec/6q36tSx8y9IsExi4L.HtmokW9rX8VehLxhg542mNTBKqxMBF.LgnCTm4.
```

# Monitoring

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | AMS DC1 DC1_POD1 DC1-POD1-SPINE2 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD1 DC1-POD1-SPINE2
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1/1 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet30/1 | routed | - | 172.17.2.100/31 | default | 9214 | false | - | - |
| Ethernet1/2 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet30/2 | routed | - | 172.17.2.102/31 | default | 9214 | false | - | - |
| Ethernet1/3 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet30/1 | routed | - | 172.17.2.132/31 | default | 9214 | false | - | - |
| Ethernet1/4 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet30/2 | routed | - | 172.17.2.134/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet30/1 | routed | - | 172.17.2.164/31 | default | 9214 | false | - | - |
| Ethernet2/2 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet30/2 | routed | - | 172.17.2.166/31 | default | 9214 | false | - | - |
| Ethernet2/3 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet30/1 | routed | - | 172.17.2.196/31 | default | 9214 | false | - | - |
| Ethernet2/4 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet30/2 | routed | - | 172.17.2.198/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet30/1 | routed | - | 172.17.2.228/31 | default | 9214 | false | - | - |
| Ethernet3/2 | P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet30/2 | routed | - | 172.17.2.230/31 | default | 9214 | false | - | - |
| Ethernet3/3 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet30/1 | routed | - | 172.17.3.4/31 | default | 9214 | false | - | - |
| Ethernet3/4 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet30/2 | routed | - | 172.17.3.6/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet30/1 | routed | - | 172.17.3.36/31 | default | 9214 | false | - | - |
| Ethernet4/2 | P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet30/2 | routed | - | 172.17.3.38/31 | default | 9214 | false | - | - |
| Ethernet4/3 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet30/1 | routed | - | 172.17.3.68/31 | default | 9214 | false | - | - |
| Ethernet4/4 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet30/2 | routed | - | 172.17.3.70/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet30/1 | routed | - | 172.17.3.100/31 | default | 9214 | false | - | - |
| Ethernet5/2 | P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet30/2 | routed | - | 172.17.3.102/31 | default | 9214 | false | - | - |
| Ethernet5/3 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet30/1 | routed | - | 172.17.3.132/31 | default | 9214 | false | - | - |
| Ethernet5/4 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet30/2 | routed | - | 172.17.3.134/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet30/1 | routed | - | 172.17.3.164/31 | default | 9214 | false | - | - |
| Ethernet6/2 | P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet30/2 | routed | - | 172.17.3.166/31 | default | 9214 | false | - | - |
| Ethernet6/3 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet30/1 | routed | - | 172.17.3.196/31 | default | 9214 | false | - | - |
| Ethernet6/4 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet30/2 | routed | - | 172.17.3.198/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet30/1 | routed | - | 172.17.3.228/31 | default | 9214 | false | - | - |
| Ethernet7/2 | P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet30/2 | routed | - | 172.17.3.230/31 | default | 9214 | false | - | - |
| Ethernet7/3 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet30/1 | routed | - | 172.17.4.4/31 | default | 9214 | false | - | - |
| Ethernet7/4 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet30/2 | routed | - | 172.17.4.6/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet30/1 | routed | - | 172.17.4.36/31 | default | 9214 | false | - | - |
| Ethernet8/2 | P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet30/2 | routed | - | 172.17.4.38/31 | default | 9214 | false | - | - |
| Ethernet8/3 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet30/1 | routed | - | 172.17.4.68/31 | default | 9214 | false | - | - |
| Ethernet8/4 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet30/2 | routed | - | 172.17.4.70/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet30/1 | routed | - | 172.17.4.100/31 | default | 9214 | false | - | - |
| Ethernet9/2 | P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet30/2 | routed | - | 172.17.4.102/31 | default | 9214 | false | - | - |
| Ethernet9/3 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet30/1 | routed | - | 172.17.4.132/31 | default | 9214 | false | - | - |
| Ethernet9/4 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet30/2 | routed | - | 172.17.4.134/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet30/1 | routed | - | 172.17.4.164/31 | default | 9214 | false | - | - |
| Ethernet10/2 | P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet30/2 | routed | - | 172.17.4.166/31 | default | 9214 | false | - | - |
| Ethernet10/3 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet30/1 | routed | - | 172.17.4.196/31 | default | 9214 | false | - | - |
| Ethernet10/4 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet30/2 | routed | - | 172.17.4.198/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet30/1 | routed | - | 172.17.4.228/31 | default | 9214 | false | - | - |
| Ethernet11/2 | P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet30/2 | routed | - | 172.17.4.230/31 | default | 9214 | false | - | - |
| Ethernet11/3 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet30/1 | routed | - | 172.17.5.4/31 | default | 9214 | false | - | - |
| Ethernet11/4 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet30/2 | routed | - | 172.17.5.6/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet30/1 | routed | - | 172.17.5.36/31 | default | 9214 | false | - | - |
| Ethernet12/2 | P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet30/2 | routed | - | 172.17.5.38/31 | default | 9214 | false | - | - |
| Ethernet12/3 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet30/1 | routed | - | 172.17.5.68/31 | default | 9214 | false | - | - |
| Ethernet12/4 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet30/2 | routed | - | 172.17.5.70/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet30/1 | routed | - | 172.17.5.100/31 | default | 9214 | false | - | - |
| Ethernet13/2 | P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet30/2 | routed | - | 172.17.5.102/31 | default | 9214 | false | - | - |
| Ethernet13/3 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet30/1 | routed | - | 172.17.5.132/31 | default | 9214 | false | - | - |
| Ethernet13/4 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet30/2 | routed | - | 172.17.5.134/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet30/1 | routed | - | 172.17.5.164/31 | default | 9214 | false | - | - |
| Ethernet14/2 | P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet30/2 | routed | - | 172.17.5.166/31 | default | 9214 | false | - | - |
| Ethernet14/3 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet30/1 | routed | - | 172.17.5.196/31 | default | 9214 | false | - | - |
| Ethernet14/4 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet30/2 | routed | - | 172.17.5.198/31 | default | 9214 | false | - | - |
| Ethernet29/2 | P2P_LINK_TO_SUPER-SPINE1_Ethernet2/1 | routed | - | 172.16.0.21/31 | default | 9214 | false | - | - |
| Ethernet30/2 | P2P_LINK_TO_SUPER-SPINE2_Ethernet2/1 | routed | - | 172.16.0.29/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet2/1 | routed | - | 172.16.0.37/31 | default | 9214 | false | - | - |
| Ethernet32/2 | P2P_LINK_TO_SUPER-SPINE4_Ethernet2/1 | routed | - | 172.16.0.45/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.100/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/2
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.102/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/3
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.132/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/4
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.134/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.164/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/2
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.166/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/3
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.196/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/4
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.198/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.228/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/2
   description P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.230/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/3
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.4/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/4
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.6/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.36/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/2
   description P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.38/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/3
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.68/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/4
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.70/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.100/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/2
   description P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.102/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/3
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.132/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/4
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.134/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.164/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/2
   description P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.166/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/3
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.196/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/4
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.198/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.228/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/2
   description P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.230/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/3
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.4/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/4
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.6/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.36/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/2
   description P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.38/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/3
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.68/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/4
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.70/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.100/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/2
   description P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.102/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/3
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.132/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/4
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.134/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.164/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/2
   description P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.166/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/3
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.196/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/4
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.198/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.228/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/2
   description P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.230/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/3
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.4/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/4
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.6/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.36/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/2
   description P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.38/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/3
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.68/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/4
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.70/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.100/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/2
   description P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.102/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/3
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.132/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/4
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.134/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.164/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/2
   description P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.166/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/3
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet30/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.196/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/4
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet30/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.198/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/2
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet2/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.21/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/2
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet2/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.29/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet2/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.37/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/2
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet2/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.45/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.0.11/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.4.0.11/32
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| mgmt | false |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf mgmt
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| mgmt | false |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| mgmt  | 0.0.0.0/0 |  10.6.1.1  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 10.6.1.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 64602|  10.4.0.11 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- |
| 172.16.0.20 | 64501 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.28 | 64502 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.36 | 64503 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.44 | 64504 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.101 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.103 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.133 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.135 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.165 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.167 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.197 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.199 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.229 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.231 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.5 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.7 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.37 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.39 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.69 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.71 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.101 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.103 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.133 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.135 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.165 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.167 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.197 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.199 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.229 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.231 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.5 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.7 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.37 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.39 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.69 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.71 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.101 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.103 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.133 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.135 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.165 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.167 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.197 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.199 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.229 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.231 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.5 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.7 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.37 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.39 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.69 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.71 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.101 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.103 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.133 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.135 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.165 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.167 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.197 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.199 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |

### Router BGP Device Configuration

```eos
!
router bgp 64602
   router-id 10.4.0.11
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.0.20 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.20 remote-as 64501
   neighbor 172.16.0.20 description SUPER-SPINE1_Ethernet2/1
   neighbor 172.16.0.28 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.28 remote-as 64502
   neighbor 172.16.0.28 description SUPER-SPINE2_Ethernet2/1
   neighbor 172.16.0.36 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.36 remote-as 64503
   neighbor 172.16.0.36 description SUPER-SPINE3_Ethernet2/1
   neighbor 172.16.0.44 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.44 remote-as 64504
   neighbor 172.16.0.44 description SUPER-SPINE4_Ethernet2/1
   neighbor 172.17.2.101 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.101 remote-as 64901
   neighbor 172.17.2.101 description DC1-POD1-LEAF1A_Ethernet30/1
   neighbor 172.17.2.103 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.103 remote-as 64901
   neighbor 172.17.2.103 description DC1-POD1-LEAF1A_Ethernet30/2
   neighbor 172.17.2.133 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.133 remote-as 64901
   neighbor 172.17.2.133 description DC1-POD1-LEAF1B_Ethernet30/1
   neighbor 172.17.2.135 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.135 remote-as 64901
   neighbor 172.17.2.135 description DC1-POD1-LEAF1B_Ethernet30/2
   neighbor 172.17.2.165 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.165 remote-as 64902
   neighbor 172.17.2.165 description DC1-POD1-LEAF2A_Ethernet30/1
   neighbor 172.17.2.167 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.167 remote-as 64902
   neighbor 172.17.2.167 description DC1-POD1-LEAF2A_Ethernet30/2
   neighbor 172.17.2.197 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.197 remote-as 64902
   neighbor 172.17.2.197 description DC1-POD1-LEAF2B_Ethernet30/1
   neighbor 172.17.2.199 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.199 remote-as 64902
   neighbor 172.17.2.199 description DC1-POD1-LEAF2B_Ethernet30/2
   neighbor 172.17.2.229 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.229 remote-as 64903
   neighbor 172.17.2.229 description DC1-POD1-LEAF3A_Ethernet30/1
   neighbor 172.17.2.231 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.231 remote-as 64903
   neighbor 172.17.2.231 description DC1-POD1-LEAF3A_Ethernet30/2
   neighbor 172.17.3.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.5 remote-as 64903
   neighbor 172.17.3.5 description DC1-POD1-LEAF3B_Ethernet30/1
   neighbor 172.17.3.7 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.7 remote-as 64903
   neighbor 172.17.3.7 description DC1-POD1-LEAF3B_Ethernet30/2
   neighbor 172.17.3.37 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.37 remote-as 64904
   neighbor 172.17.3.37 description DC1-POD1-LEAF4A_Ethernet30/1
   neighbor 172.17.3.39 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.39 remote-as 64904
   neighbor 172.17.3.39 description DC1-POD1-LEAF4A_Ethernet30/2
   neighbor 172.17.3.69 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.69 remote-as 64904
   neighbor 172.17.3.69 description DC1-POD1-LEAF4B_Ethernet30/1
   neighbor 172.17.3.71 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.71 remote-as 64904
   neighbor 172.17.3.71 description DC1-POD1-LEAF4B_Ethernet30/2
   neighbor 172.17.3.101 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.101 remote-as 64905
   neighbor 172.17.3.101 description DC1-POD1-LEAF5A_Ethernet30/1
   neighbor 172.17.3.103 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.103 remote-as 64905
   neighbor 172.17.3.103 description DC1-POD1-LEAF5A_Ethernet30/2
   neighbor 172.17.3.133 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.133 remote-as 64905
   neighbor 172.17.3.133 description DC1-POD1-LEAF5B_Ethernet30/1
   neighbor 172.17.3.135 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.135 remote-as 64905
   neighbor 172.17.3.135 description DC1-POD1-LEAF5B_Ethernet30/2
   neighbor 172.17.3.165 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.165 remote-as 64906
   neighbor 172.17.3.165 description DC1-POD1-LEAF6A_Ethernet30/1
   neighbor 172.17.3.167 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.167 remote-as 64906
   neighbor 172.17.3.167 description DC1-POD1-LEAF6A_Ethernet30/2
   neighbor 172.17.3.197 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.197 remote-as 64906
   neighbor 172.17.3.197 description DC1-POD1-LEAF6B_Ethernet30/1
   neighbor 172.17.3.199 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.199 remote-as 64906
   neighbor 172.17.3.199 description DC1-POD1-LEAF6B_Ethernet30/2
   neighbor 172.17.3.229 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.229 remote-as 64907
   neighbor 172.17.3.229 description DC1-POD1-LEAF7A_Ethernet30/1
   neighbor 172.17.3.231 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.231 remote-as 64907
   neighbor 172.17.3.231 description DC1-POD1-LEAF7A_Ethernet30/2
   neighbor 172.17.4.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.5 remote-as 64907
   neighbor 172.17.4.5 description DC1-POD1-LEAF7B_Ethernet30/1
   neighbor 172.17.4.7 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.7 remote-as 64907
   neighbor 172.17.4.7 description DC1-POD1-LEAF7B_Ethernet30/2
   neighbor 172.17.4.37 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.37 remote-as 64908
   neighbor 172.17.4.37 description DC1-POD1-LEAF8A_Ethernet30/1
   neighbor 172.17.4.39 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.39 remote-as 64908
   neighbor 172.17.4.39 description DC1-POD1-LEAF8A_Ethernet30/2
   neighbor 172.17.4.69 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.69 remote-as 64908
   neighbor 172.17.4.69 description DC1-POD1-LEAF8B_Ethernet30/1
   neighbor 172.17.4.71 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.71 remote-as 64908
   neighbor 172.17.4.71 description DC1-POD1-LEAF8B_Ethernet30/2
   neighbor 172.17.4.101 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.101 remote-as 64909
   neighbor 172.17.4.101 description DC1-POD1-LEAF9A_Ethernet30/1
   neighbor 172.17.4.103 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.103 remote-as 64909
   neighbor 172.17.4.103 description DC1-POD1-LEAF9A_Ethernet30/2
   neighbor 172.17.4.133 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.133 remote-as 64909
   neighbor 172.17.4.133 description DC1-POD1-LEAF9B_Ethernet30/1
   neighbor 172.17.4.135 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.135 remote-as 64909
   neighbor 172.17.4.135 description DC1-POD1-LEAF9B_Ethernet30/2
   neighbor 172.17.4.165 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.165 remote-as 64910
   neighbor 172.17.4.165 description DC1-POD1-LEAF10A_Ethernet30/1
   neighbor 172.17.4.167 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.167 remote-as 64910
   neighbor 172.17.4.167 description DC1-POD1-LEAF10A_Ethernet30/2
   neighbor 172.17.4.197 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.197 remote-as 64910
   neighbor 172.17.4.197 description DC1-POD1-LEAF10B_Ethernet30/1
   neighbor 172.17.4.199 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.199 remote-as 64910
   neighbor 172.17.4.199 description DC1-POD1-LEAF10B_Ethernet30/2
   neighbor 172.17.4.229 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.229 remote-as 64911
   neighbor 172.17.4.229 description DC1-POD1-LEAF11A_Ethernet30/1
   neighbor 172.17.4.231 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.231 remote-as 64911
   neighbor 172.17.4.231 description DC1-POD1-LEAF11A_Ethernet30/2
   neighbor 172.17.5.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.5 remote-as 64911
   neighbor 172.17.5.5 description DC1-POD1-LEAF11B_Ethernet30/1
   neighbor 172.17.5.7 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.7 remote-as 64911
   neighbor 172.17.5.7 description DC1-POD1-LEAF11B_Ethernet30/2
   neighbor 172.17.5.37 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.37 remote-as 64912
   neighbor 172.17.5.37 description DC1-POD1-LEAF12A_Ethernet30/1
   neighbor 172.17.5.39 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.39 remote-as 64912
   neighbor 172.17.5.39 description DC1-POD1-LEAF12A_Ethernet30/2
   neighbor 172.17.5.69 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.69 remote-as 64912
   neighbor 172.17.5.69 description DC1-POD1-LEAF12B_Ethernet30/1
   neighbor 172.17.5.71 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.71 remote-as 64912
   neighbor 172.17.5.71 description DC1-POD1-LEAF12B_Ethernet30/2
   neighbor 172.17.5.101 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.101 remote-as 64913
   neighbor 172.17.5.101 description DC1-POD1-LEAF13A_Ethernet30/1
   neighbor 172.17.5.103 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.103 remote-as 64913
   neighbor 172.17.5.103 description DC1-POD1-LEAF13A_Ethernet30/2
   neighbor 172.17.5.133 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.133 remote-as 64913
   neighbor 172.17.5.133 description DC1-POD1-LEAF13B_Ethernet30/1
   neighbor 172.17.5.135 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.135 remote-as 64913
   neighbor 172.17.5.135 description DC1-POD1-LEAF13B_Ethernet30/2
   neighbor 172.17.5.165 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.165 remote-as 64914
   neighbor 172.17.5.165 description DC1-POD1-LEAF14A_Ethernet30/1
   neighbor 172.17.5.167 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.167 remote-as 64914
   neighbor 172.17.5.167 description DC1-POD1-LEAF14A_Ethernet30/2
   neighbor 172.17.5.197 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.197 remote-as 64914
   neighbor 172.17.5.197 description DC1-POD1-LEAF14B_Ethernet30/1
   neighbor 172.17.5.199 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.199 remote-as 64914
   neighbor 172.17.5.199 description DC1-POD1-LEAF14B_Ethernet30/2
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
```

# Multicast

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.4.0.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.0.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| mgmt | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance mgmt
```

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB in AMS.yml

```
