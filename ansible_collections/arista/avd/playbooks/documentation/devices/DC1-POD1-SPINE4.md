# DC1-POD1-SPINE4
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
| Management0 | oob_management | oob | mgmt | 10.6.1.13/24 | 10.6.1.1 |

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
   ip address 10.6.1.13/24
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
| - | AMS DC1 DC1_POD1 DC1-POD1-SPINE4 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD1 DC1-POD1-SPINE4
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
| Ethernet1/2 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet32/2 | routed | - | 172.17.2.110/31 | default | 9214 | false | - | - |
| Ethernet1/3 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet32/1 | routed | - | 172.17.2.140/31 | default | 9214 | false | - | - |
| Ethernet1/4 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet32/2 | routed | - | 172.17.2.142/31 | default | 9214 | false | - | - |
| Ethernet2/2 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet32/2 | routed | - | 172.17.2.174/31 | default | 9214 | false | - | - |
| Ethernet2/3 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet32/1 | routed | - | 172.17.2.204/31 | default | 9214 | false | - | - |
| Ethernet2/4 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet32/2 | routed | - | 172.17.2.206/31 | default | 9214 | false | - | - |
| Ethernet3/2 | P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet32/2 | routed | - | 172.17.2.238/31 | default | 9214 | false | - | - |
| Ethernet3/3 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet32/1 | routed | - | 172.17.3.12/31 | default | 9214 | false | - | - |
| Ethernet3/4 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet32/2 | routed | - | 172.17.3.14/31 | default | 9214 | false | - | - |
| Ethernet4/2 | P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet32/2 | routed | - | 172.17.3.46/31 | default | 9214 | false | - | - |
| Ethernet4/3 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet32/1 | routed | - | 172.17.3.76/31 | default | 9214 | false | - | - |
| Ethernet4/4 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet32/2 | routed | - | 172.17.3.78/31 | default | 9214 | false | - | - |
| Ethernet5/2 | P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet32/2 | routed | - | 172.17.3.110/31 | default | 9214 | false | - | - |
| Ethernet5/3 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet32/1 | routed | - | 172.17.3.140/31 | default | 9214 | false | - | - |
| Ethernet5/4 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet32/2 | routed | - | 172.17.3.142/31 | default | 9214 | false | - | - |
| Ethernet6/2 | P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet32/2 | routed | - | 172.17.3.174/31 | default | 9214 | false | - | - |
| Ethernet6/3 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet32/1 | routed | - | 172.17.3.204/31 | default | 9214 | false | - | - |
| Ethernet6/4 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet32/2 | routed | - | 172.17.3.206/31 | default | 9214 | false | - | - |
| Ethernet7/2 | P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet32/2 | routed | - | 172.17.3.238/31 | default | 9214 | false | - | - |
| Ethernet7/3 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet32/1 | routed | - | 172.17.4.12/31 | default | 9214 | false | - | - |
| Ethernet7/4 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet32/2 | routed | - | 172.17.4.14/31 | default | 9214 | false | - | - |
| Ethernet8/2 | P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet32/2 | routed | - | 172.17.4.46/31 | default | 9214 | false | - | - |
| Ethernet8/3 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet32/1 | routed | - | 172.17.4.76/31 | default | 9214 | false | - | - |
| Ethernet8/4 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet32/2 | routed | - | 172.17.4.78/31 | default | 9214 | false | - | - |
| Ethernet9/2 | P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet32/2 | routed | - | 172.17.4.110/31 | default | 9214 | false | - | - |
| Ethernet9/3 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet32/1 | routed | - | 172.17.4.140/31 | default | 9214 | false | - | - |
| Ethernet9/4 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet32/2 | routed | - | 172.17.4.142/31 | default | 9214 | false | - | - |
| Ethernet10/2 | P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet32/2 | routed | - | 172.17.4.174/31 | default | 9214 | false | - | - |
| Ethernet10/3 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet32/1 | routed | - | 172.17.4.204/31 | default | 9214 | false | - | - |
| Ethernet10/4 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet32/2 | routed | - | 172.17.4.206/31 | default | 9214 | false | - | - |
| Ethernet11/2 | P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet32/2 | routed | - | 172.17.4.238/31 | default | 9214 | false | - | - |
| Ethernet11/3 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet32/1 | routed | - | 172.17.5.12/31 | default | 9214 | false | - | - |
| Ethernet11/4 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet32/2 | routed | - | 172.17.5.14/31 | default | 9214 | false | - | - |
| Ethernet12/2 | P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet32/2 | routed | - | 172.17.5.46/31 | default | 9214 | false | - | - |
| Ethernet12/3 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet32/1 | routed | - | 172.17.5.76/31 | default | 9214 | false | - | - |
| Ethernet12/4 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet32/2 | routed | - | 172.17.5.78/31 | default | 9214 | false | - | - |
| Ethernet13/2 | P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet32/2 | routed | - | 172.17.5.110/31 | default | 9214 | false | - | - |
| Ethernet13/3 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet32/1 | routed | - | 172.17.5.140/31 | default | 9214 | false | - | - |
| Ethernet13/4 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet32/2 | routed | - | 172.17.5.142/31 | default | 9214 | false | - | - |
| Ethernet14/2 | P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet32/2 | routed | - | 172.17.5.174/31 | default | 9214 | false | - | - |
| Ethernet14/3 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet32/1 | routed | - | 172.17.5.204/31 | default | 9214 | false | - | - |
| Ethernet14/4 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet32/2 | routed | - | 172.17.5.206/31 | default | 9214 | false | - | - |
| Ethernet29/2 | P2P_LINK_TO_SUPER-SPINE1_Ethernet4/1 | routed | - | 172.16.0.25/31 | default | 9214 | false | - | - |
| Ethernet30/2 | P2P_LINK_TO_SUPER-SPINE2_Ethernet4/1 | routed | - | 172.16.0.33/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet4/1 | routed | - | 172.16.0.41/31 | default | 9214 | false | - | - |
| Ethernet32/2 | P2P_LINK_TO_SUPER-SPINE4_Ethernet4/1 | routed | - | 172.16.0.49/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/2
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.110/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/3
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.140/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/4
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.142/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/2
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.174/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/3
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.204/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/4
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.206/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/2
   description P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.238/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/3
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.12/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/4
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.14/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/2
   description P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.46/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/3
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.76/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/4
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.78/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/2
   description P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.110/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/3
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.140/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/4
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.142/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/2
   description P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.174/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/3
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.204/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/4
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.206/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/2
   description P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.238/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/3
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.12/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/4
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.14/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/2
   description P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.46/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/3
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.76/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/4
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.78/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/2
   description P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.110/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/3
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.140/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/4
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.142/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/2
   description P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.174/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/3
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.204/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/4
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.206/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/2
   description P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.238/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/3
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.12/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/4
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.14/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/2
   description P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.46/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/3
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.76/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/4
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.78/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/2
   description P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.110/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/3
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.140/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/4
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.142/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/2
   description P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.174/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/3
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet32/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.204/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/4
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet32/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.206/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/2
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet4/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.25/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/2
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet4/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.33/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet4/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.41/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/2
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet4/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.49/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.0.13/32 |

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
   ip address 10.4.0.13/32
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
| 64604|  10.4.0.13 |

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
| 172.16.0.24 | 64501 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.32 | 64502 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.40 | 64503 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.48 | 64504 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.111 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.141 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.143 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.175 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.205 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.207 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.239 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.13 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.15 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.47 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.77 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.79 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.111 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.141 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.143 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.175 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.205 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.207 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.239 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.13 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.15 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.47 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.77 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.79 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.111 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.141 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.143 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.175 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.205 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.207 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.239 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.13 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.15 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.47 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.77 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.79 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.111 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.141 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.143 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.175 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.205 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.207 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |

### Router BGP Device Configuration

```eos
!
router bgp 64604
   router-id 10.4.0.13
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.0.24 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.24 remote-as 64501
   neighbor 172.16.0.24 description SUPER-SPINE1_Ethernet4/1
   neighbor 172.16.0.32 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.32 remote-as 64502
   neighbor 172.16.0.32 description SUPER-SPINE2_Ethernet4/1
   neighbor 172.16.0.40 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.40 remote-as 64503
   neighbor 172.16.0.40 description SUPER-SPINE3_Ethernet4/1
   neighbor 172.16.0.48 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.48 remote-as 64504
   neighbor 172.16.0.48 description SUPER-SPINE4_Ethernet4/1
   neighbor 172.17.2.111 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.111 remote-as 64901
   neighbor 172.17.2.111 description DC1-POD1-LEAF1A_Ethernet32/2
   neighbor 172.17.2.141 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.141 remote-as 64901
   neighbor 172.17.2.141 description DC1-POD1-LEAF1B_Ethernet32/1
   neighbor 172.17.2.143 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.143 remote-as 64901
   neighbor 172.17.2.143 description DC1-POD1-LEAF1B_Ethernet32/2
   neighbor 172.17.2.175 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.175 remote-as 64902
   neighbor 172.17.2.175 description DC1-POD1-LEAF2A_Ethernet32/2
   neighbor 172.17.2.205 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.205 remote-as 64902
   neighbor 172.17.2.205 description DC1-POD1-LEAF2B_Ethernet32/1
   neighbor 172.17.2.207 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.207 remote-as 64902
   neighbor 172.17.2.207 description DC1-POD1-LEAF2B_Ethernet32/2
   neighbor 172.17.2.239 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.239 remote-as 64903
   neighbor 172.17.2.239 description DC1-POD1-LEAF3A_Ethernet32/2
   neighbor 172.17.3.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.13 remote-as 64903
   neighbor 172.17.3.13 description DC1-POD1-LEAF3B_Ethernet32/1
   neighbor 172.17.3.15 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.15 remote-as 64903
   neighbor 172.17.3.15 description DC1-POD1-LEAF3B_Ethernet32/2
   neighbor 172.17.3.47 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.47 remote-as 64904
   neighbor 172.17.3.47 description DC1-POD1-LEAF4A_Ethernet32/2
   neighbor 172.17.3.77 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.77 remote-as 64904
   neighbor 172.17.3.77 description DC1-POD1-LEAF4B_Ethernet32/1
   neighbor 172.17.3.79 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.79 remote-as 64904
   neighbor 172.17.3.79 description DC1-POD1-LEAF4B_Ethernet32/2
   neighbor 172.17.3.111 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.111 remote-as 64905
   neighbor 172.17.3.111 description DC1-POD1-LEAF5A_Ethernet32/2
   neighbor 172.17.3.141 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.141 remote-as 64905
   neighbor 172.17.3.141 description DC1-POD1-LEAF5B_Ethernet32/1
   neighbor 172.17.3.143 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.143 remote-as 64905
   neighbor 172.17.3.143 description DC1-POD1-LEAF5B_Ethernet32/2
   neighbor 172.17.3.175 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.175 remote-as 64906
   neighbor 172.17.3.175 description DC1-POD1-LEAF6A_Ethernet32/2
   neighbor 172.17.3.205 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.205 remote-as 64906
   neighbor 172.17.3.205 description DC1-POD1-LEAF6B_Ethernet32/1
   neighbor 172.17.3.207 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.207 remote-as 64906
   neighbor 172.17.3.207 description DC1-POD1-LEAF6B_Ethernet32/2
   neighbor 172.17.3.239 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.239 remote-as 64907
   neighbor 172.17.3.239 description DC1-POD1-LEAF7A_Ethernet32/2
   neighbor 172.17.4.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.13 remote-as 64907
   neighbor 172.17.4.13 description DC1-POD1-LEAF7B_Ethernet32/1
   neighbor 172.17.4.15 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.15 remote-as 64907
   neighbor 172.17.4.15 description DC1-POD1-LEAF7B_Ethernet32/2
   neighbor 172.17.4.47 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.47 remote-as 64908
   neighbor 172.17.4.47 description DC1-POD1-LEAF8A_Ethernet32/2
   neighbor 172.17.4.77 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.77 remote-as 64908
   neighbor 172.17.4.77 description DC1-POD1-LEAF8B_Ethernet32/1
   neighbor 172.17.4.79 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.79 remote-as 64908
   neighbor 172.17.4.79 description DC1-POD1-LEAF8B_Ethernet32/2
   neighbor 172.17.4.111 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.111 remote-as 64909
   neighbor 172.17.4.111 description DC1-POD1-LEAF9A_Ethernet32/2
   neighbor 172.17.4.141 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.141 remote-as 64909
   neighbor 172.17.4.141 description DC1-POD1-LEAF9B_Ethernet32/1
   neighbor 172.17.4.143 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.143 remote-as 64909
   neighbor 172.17.4.143 description DC1-POD1-LEAF9B_Ethernet32/2
   neighbor 172.17.4.175 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.175 remote-as 64910
   neighbor 172.17.4.175 description DC1-POD1-LEAF10A_Ethernet32/2
   neighbor 172.17.4.205 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.205 remote-as 64910
   neighbor 172.17.4.205 description DC1-POD1-LEAF10B_Ethernet32/1
   neighbor 172.17.4.207 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.207 remote-as 64910
   neighbor 172.17.4.207 description DC1-POD1-LEAF10B_Ethernet32/2
   neighbor 172.17.4.239 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.239 remote-as 64911
   neighbor 172.17.4.239 description DC1-POD1-LEAF11A_Ethernet32/2
   neighbor 172.17.5.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.13 remote-as 64911
   neighbor 172.17.5.13 description DC1-POD1-LEAF11B_Ethernet32/1
   neighbor 172.17.5.15 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.15 remote-as 64911
   neighbor 172.17.5.15 description DC1-POD1-LEAF11B_Ethernet32/2
   neighbor 172.17.5.47 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.47 remote-as 64912
   neighbor 172.17.5.47 description DC1-POD1-LEAF12A_Ethernet32/2
   neighbor 172.17.5.77 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.77 remote-as 64912
   neighbor 172.17.5.77 description DC1-POD1-LEAF12B_Ethernet32/1
   neighbor 172.17.5.79 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.79 remote-as 64912
   neighbor 172.17.5.79 description DC1-POD1-LEAF12B_Ethernet32/2
   neighbor 172.17.5.111 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.111 remote-as 64913
   neighbor 172.17.5.111 description DC1-POD1-LEAF13A_Ethernet32/2
   neighbor 172.17.5.141 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.141 remote-as 64913
   neighbor 172.17.5.141 description DC1-POD1-LEAF13B_Ethernet32/1
   neighbor 172.17.5.143 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.143 remote-as 64913
   neighbor 172.17.5.143 description DC1-POD1-LEAF13B_Ethernet32/2
   neighbor 172.17.5.175 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.175 remote-as 64914
   neighbor 172.17.5.175 description DC1-POD1-LEAF14A_Ethernet32/2
   neighbor 172.17.5.205 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.205 remote-as 64914
   neighbor 172.17.5.205 description DC1-POD1-LEAF14B_Ethernet32/1
   neighbor 172.17.5.207 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.207 remote-as 64914
   neighbor 172.17.5.207 description DC1-POD1-LEAF14B_Ethernet32/2
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
