# DC1-POD1-SPINE3
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
| Management0 | oob_management | oob | mgmt | 10.6.1.12/24 | 10.6.1.1 |

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
   ip address 10.6.1.12/24
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
| - | AMS DC1 DC1_POD1 DC1-POD1-SPINE3 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD1 DC1-POD1-SPINE3
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
| Ethernet1/1 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet31/1 | routed | - | 172.17.2.104/31 | default | 9214 | false | - | - |
| Ethernet1/2 | P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet31/2 | routed | - | 172.17.2.106/31 | default | 9214 | false | - | - |
| Ethernet1/3 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet31/1 | routed | - | 172.17.2.136/31 | default | 9214 | false | - | - |
| Ethernet1/4 | P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet31/2 | routed | - | 172.17.2.138/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet31/1 | routed | - | 172.17.2.168/31 | default | 9214 | false | - | - |
| Ethernet2/2 | P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet31/2 | routed | - | 172.17.2.170/31 | default | 9214 | false | - | - |
| Ethernet2/3 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet31/1 | routed | - | 172.17.2.200/31 | default | 9214 | false | - | - |
| Ethernet2/4 | P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet31/2 | routed | - | 172.17.2.202/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet31/1 | routed | - | 172.17.2.232/31 | default | 9214 | false | - | - |
| Ethernet3/2 | P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet31/2 | routed | - | 172.17.2.234/31 | default | 9214 | false | - | - |
| Ethernet3/3 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet31/1 | routed | - | 172.17.3.8/31 | default | 9214 | false | - | - |
| Ethernet3/4 | P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet31/2 | routed | - | 172.17.3.10/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet31/1 | routed | - | 172.17.3.40/31 | default | 9214 | false | - | - |
| Ethernet4/2 | P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet31/2 | routed | - | 172.17.3.42/31 | default | 9214 | false | - | - |
| Ethernet4/3 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet31/1 | routed | - | 172.17.3.72/31 | default | 9214 | false | - | - |
| Ethernet4/4 | P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet31/2 | routed | - | 172.17.3.74/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet31/1 | routed | - | 172.17.3.104/31 | default | 9214 | false | - | - |
| Ethernet5/2 | P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet31/2 | routed | - | 172.17.3.106/31 | default | 9214 | false | - | - |
| Ethernet5/3 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet31/1 | routed | - | 172.17.3.136/31 | default | 9214 | false | - | - |
| Ethernet5/4 | P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet31/2 | routed | - | 172.17.3.138/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet31/1 | routed | - | 172.17.3.168/31 | default | 9214 | false | - | - |
| Ethernet6/2 | P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet31/2 | routed | - | 172.17.3.170/31 | default | 9214 | false | - | - |
| Ethernet6/3 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet31/1 | routed | - | 172.17.3.200/31 | default | 9214 | false | - | - |
| Ethernet6/4 | P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet31/2 | routed | - | 172.17.3.202/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet31/1 | routed | - | 172.17.3.232/31 | default | 9214 | false | - | - |
| Ethernet7/2 | P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet31/2 | routed | - | 172.17.3.234/31 | default | 9214 | false | - | - |
| Ethernet7/3 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet31/1 | routed | - | 172.17.4.8/31 | default | 9214 | false | - | - |
| Ethernet7/4 | P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet31/2 | routed | - | 172.17.4.10/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet31/1 | routed | - | 172.17.4.40/31 | default | 9214 | false | - | - |
| Ethernet8/2 | P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet31/2 | routed | - | 172.17.4.42/31 | default | 9214 | false | - | - |
| Ethernet8/3 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet31/1 | routed | - | 172.17.4.72/31 | default | 9214 | false | - | - |
| Ethernet8/4 | P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet31/2 | routed | - | 172.17.4.74/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet31/1 | routed | - | 172.17.4.104/31 | default | 9214 | false | - | - |
| Ethernet9/2 | P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet31/2 | routed | - | 172.17.4.106/31 | default | 9214 | false | - | - |
| Ethernet9/3 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet31/1 | routed | - | 172.17.4.136/31 | default | 9214 | false | - | - |
| Ethernet9/4 | P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet31/2 | routed | - | 172.17.4.138/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet31/1 | routed | - | 172.17.4.168/31 | default | 9214 | false | - | - |
| Ethernet10/2 | P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet31/2 | routed | - | 172.17.4.170/31 | default | 9214 | false | - | - |
| Ethernet10/3 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet31/1 | routed | - | 172.17.4.200/31 | default | 9214 | false | - | - |
| Ethernet10/4 | P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet31/2 | routed | - | 172.17.4.202/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet31/1 | routed | - | 172.17.4.232/31 | default | 9214 | false | - | - |
| Ethernet11/2 | P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet31/2 | routed | - | 172.17.4.234/31 | default | 9214 | false | - | - |
| Ethernet11/3 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet31/1 | routed | - | 172.17.5.8/31 | default | 9214 | false | - | - |
| Ethernet11/4 | P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet31/2 | routed | - | 172.17.5.10/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet31/1 | routed | - | 172.17.5.40/31 | default | 9214 | false | - | - |
| Ethernet12/2 | P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet31/2 | routed | - | 172.17.5.42/31 | default | 9214 | false | - | - |
| Ethernet12/3 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet31/1 | routed | - | 172.17.5.72/31 | default | 9214 | false | - | - |
| Ethernet12/4 | P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet31/2 | routed | - | 172.17.5.74/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet31/1 | routed | - | 172.17.5.104/31 | default | 9214 | false | - | - |
| Ethernet13/2 | P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet31/2 | routed | - | 172.17.5.106/31 | default | 9214 | false | - | - |
| Ethernet13/3 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet31/1 | routed | - | 172.17.5.136/31 | default | 9214 | false | - | - |
| Ethernet13/4 | P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet31/2 | routed | - | 172.17.5.138/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet31/1 | routed | - | 172.17.5.168/31 | default | 9214 | false | - | - |
| Ethernet14/2 | P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet31/2 | routed | - | 172.17.5.170/31 | default | 9214 | false | - | - |
| Ethernet14/3 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet31/1 | routed | - | 172.17.5.200/31 | default | 9214 | false | - | - |
| Ethernet14/4 | P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet31/2 | routed | - | 172.17.5.202/31 | default | 9214 | false | - | - |
| Ethernet29/2 | P2P_LINK_TO_SUPER-SPINE1_Ethernet3/1 | routed | - | 172.16.0.23/31 | default | 9214 | false | - | - |
| Ethernet30/2 | P2P_LINK_TO_SUPER-SPINE2_Ethernet3/1 | routed | - | 172.16.0.31/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet3/1 | routed | - | 172.16.0.39/31 | default | 9214 | false | - | - |
| Ethernet32/2 | P2P_LINK_TO_SUPER-SPINE4_Ethernet3/1 | routed | - | 172.16.0.47/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.104/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/2
   description P2P_LINK_TO_DC1-POD1-LEAF1A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.106/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/3
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.136/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet1/4
   description P2P_LINK_TO_DC1-POD1-LEAF1B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.138/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.168/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/2
   description P2P_LINK_TO_DC1-POD1-LEAF2A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.170/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/3
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.200/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/4
   description P2P_LINK_TO_DC1-POD1-LEAF2B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.202/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.232/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/2
   description P2P_LINK_TO_DC1-POD1-LEAF3A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.2.234/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/3
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.8/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/4
   description P2P_LINK_TO_DC1-POD1-LEAF3B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.10/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.40/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/2
   description P2P_LINK_TO_DC1-POD1-LEAF4A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.42/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/3
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.72/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/4
   description P2P_LINK_TO_DC1-POD1-LEAF4B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.74/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.104/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/2
   description P2P_LINK_TO_DC1-POD1-LEAF5A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.106/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/3
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.136/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/4
   description P2P_LINK_TO_DC1-POD1-LEAF5B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.138/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.168/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/2
   description P2P_LINK_TO_DC1-POD1-LEAF6A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.170/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/3
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.200/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/4
   description P2P_LINK_TO_DC1-POD1-LEAF6B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.202/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.232/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/2
   description P2P_LINK_TO_DC1-POD1-LEAF7A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.3.234/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/3
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.8/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/4
   description P2P_LINK_TO_DC1-POD1-LEAF7B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.10/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.40/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/2
   description P2P_LINK_TO_DC1-POD1-LEAF8A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.42/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/3
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.72/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/4
   description P2P_LINK_TO_DC1-POD1-LEAF8B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.74/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.104/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/2
   description P2P_LINK_TO_DC1-POD1-LEAF9A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.106/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/3
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.136/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/4
   description P2P_LINK_TO_DC1-POD1-LEAF9B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.138/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.168/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/2
   description P2P_LINK_TO_DC1-POD1-LEAF10A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.170/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/3
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.200/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/4
   description P2P_LINK_TO_DC1-POD1-LEAF10B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.202/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.232/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/2
   description P2P_LINK_TO_DC1-POD1-LEAF11A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.4.234/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/3
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.8/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/4
   description P2P_LINK_TO_DC1-POD1-LEAF11B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.10/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.40/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/2
   description P2P_LINK_TO_DC1-POD1-LEAF12A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.42/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/3
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.72/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/4
   description P2P_LINK_TO_DC1-POD1-LEAF12B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.74/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.104/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/2
   description P2P_LINK_TO_DC1-POD1-LEAF13A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.106/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/3
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.136/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/4
   description P2P_LINK_TO_DC1-POD1-LEAF13B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.138/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.168/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/2
   description P2P_LINK_TO_DC1-POD1-LEAF14A_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.170/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/3
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet31/1
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.200/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/4
   description P2P_LINK_TO_DC1-POD1-LEAF14B_Ethernet31/2
   no shutdown
   speed forced 100g
   mtu 9214
   no switchport
   ip address 172.17.5.202/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/2
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet3/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.23/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/2
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet3/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.31/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet3/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.39/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/2
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet3/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.0.47/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.0.12/32 |

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
   ip address 10.4.0.12/32
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
| 64603|  10.4.0.12 |

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
| 172.16.0.22 | 64501 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.30 | 64502 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.38 | 64503 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.0.46 | 64504 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.105 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.107 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.137 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.139 | 64901 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.169 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.171 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.201 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.203 | 64902 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.233 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.2.235 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.9 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.11 | 64903 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.41 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.43 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.73 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.75 | 64904 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.105 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.107 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.137 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.139 | 64905 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.169 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.171 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.201 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.203 | 64906 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.233 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.3.235 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.9 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.11 | 64907 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.41 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.43 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.73 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.75 | 64908 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.105 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.107 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.137 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.139 | 64909 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.169 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.171 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.201 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.203 | 64910 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.233 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.4.235 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.9 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.11 | 64911 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.41 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.43 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.73 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.75 | 64912 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.105 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.107 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.137 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.139 | 64913 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.169 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.171 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.201 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.5.203 | 64914 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |

### Router BGP Device Configuration

```eos
!
router bgp 64603
   router-id 10.4.0.12
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.0.22 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.22 remote-as 64501
   neighbor 172.16.0.22 description SUPER-SPINE1_Ethernet3/1
   neighbor 172.16.0.30 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.30 remote-as 64502
   neighbor 172.16.0.30 description SUPER-SPINE2_Ethernet3/1
   neighbor 172.16.0.38 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.38 remote-as 64503
   neighbor 172.16.0.38 description SUPER-SPINE3_Ethernet3/1
   neighbor 172.16.0.46 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.0.46 remote-as 64504
   neighbor 172.16.0.46 description SUPER-SPINE4_Ethernet3/1
   neighbor 172.17.2.105 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.105 remote-as 64901
   neighbor 172.17.2.105 description DC1-POD1-LEAF1A_Ethernet31/1
   neighbor 172.17.2.107 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.107 remote-as 64901
   neighbor 172.17.2.107 description DC1-POD1-LEAF1A_Ethernet31/2
   neighbor 172.17.2.137 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.137 remote-as 64901
   neighbor 172.17.2.137 description DC1-POD1-LEAF1B_Ethernet31/1
   neighbor 172.17.2.139 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.139 remote-as 64901
   neighbor 172.17.2.139 description DC1-POD1-LEAF1B_Ethernet31/2
   neighbor 172.17.2.169 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.169 remote-as 64902
   neighbor 172.17.2.169 description DC1-POD1-LEAF2A_Ethernet31/1
   neighbor 172.17.2.171 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.171 remote-as 64902
   neighbor 172.17.2.171 description DC1-POD1-LEAF2A_Ethernet31/2
   neighbor 172.17.2.201 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.201 remote-as 64902
   neighbor 172.17.2.201 description DC1-POD1-LEAF2B_Ethernet31/1
   neighbor 172.17.2.203 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.203 remote-as 64902
   neighbor 172.17.2.203 description DC1-POD1-LEAF2B_Ethernet31/2
   neighbor 172.17.2.233 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.233 remote-as 64903
   neighbor 172.17.2.233 description DC1-POD1-LEAF3A_Ethernet31/1
   neighbor 172.17.2.235 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.235 remote-as 64903
   neighbor 172.17.2.235 description DC1-POD1-LEAF3A_Ethernet31/2
   neighbor 172.17.3.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.9 remote-as 64903
   neighbor 172.17.3.9 description DC1-POD1-LEAF3B_Ethernet31/1
   neighbor 172.17.3.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.11 remote-as 64903
   neighbor 172.17.3.11 description DC1-POD1-LEAF3B_Ethernet31/2
   neighbor 172.17.3.41 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.41 remote-as 64904
   neighbor 172.17.3.41 description DC1-POD1-LEAF4A_Ethernet31/1
   neighbor 172.17.3.43 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.43 remote-as 64904
   neighbor 172.17.3.43 description DC1-POD1-LEAF4A_Ethernet31/2
   neighbor 172.17.3.73 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.73 remote-as 64904
   neighbor 172.17.3.73 description DC1-POD1-LEAF4B_Ethernet31/1
   neighbor 172.17.3.75 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.75 remote-as 64904
   neighbor 172.17.3.75 description DC1-POD1-LEAF4B_Ethernet31/2
   neighbor 172.17.3.105 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.105 remote-as 64905
   neighbor 172.17.3.105 description DC1-POD1-LEAF5A_Ethernet31/1
   neighbor 172.17.3.107 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.107 remote-as 64905
   neighbor 172.17.3.107 description DC1-POD1-LEAF5A_Ethernet31/2
   neighbor 172.17.3.137 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.137 remote-as 64905
   neighbor 172.17.3.137 description DC1-POD1-LEAF5B_Ethernet31/1
   neighbor 172.17.3.139 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.139 remote-as 64905
   neighbor 172.17.3.139 description DC1-POD1-LEAF5B_Ethernet31/2
   neighbor 172.17.3.169 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.169 remote-as 64906
   neighbor 172.17.3.169 description DC1-POD1-LEAF6A_Ethernet31/1
   neighbor 172.17.3.171 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.171 remote-as 64906
   neighbor 172.17.3.171 description DC1-POD1-LEAF6A_Ethernet31/2
   neighbor 172.17.3.201 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.201 remote-as 64906
   neighbor 172.17.3.201 description DC1-POD1-LEAF6B_Ethernet31/1
   neighbor 172.17.3.203 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.203 remote-as 64906
   neighbor 172.17.3.203 description DC1-POD1-LEAF6B_Ethernet31/2
   neighbor 172.17.3.233 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.233 remote-as 64907
   neighbor 172.17.3.233 description DC1-POD1-LEAF7A_Ethernet31/1
   neighbor 172.17.3.235 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.3.235 remote-as 64907
   neighbor 172.17.3.235 description DC1-POD1-LEAF7A_Ethernet31/2
   neighbor 172.17.4.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.9 remote-as 64907
   neighbor 172.17.4.9 description DC1-POD1-LEAF7B_Ethernet31/1
   neighbor 172.17.4.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.11 remote-as 64907
   neighbor 172.17.4.11 description DC1-POD1-LEAF7B_Ethernet31/2
   neighbor 172.17.4.41 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.41 remote-as 64908
   neighbor 172.17.4.41 description DC1-POD1-LEAF8A_Ethernet31/1
   neighbor 172.17.4.43 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.43 remote-as 64908
   neighbor 172.17.4.43 description DC1-POD1-LEAF8A_Ethernet31/2
   neighbor 172.17.4.73 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.73 remote-as 64908
   neighbor 172.17.4.73 description DC1-POD1-LEAF8B_Ethernet31/1
   neighbor 172.17.4.75 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.75 remote-as 64908
   neighbor 172.17.4.75 description DC1-POD1-LEAF8B_Ethernet31/2
   neighbor 172.17.4.105 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.105 remote-as 64909
   neighbor 172.17.4.105 description DC1-POD1-LEAF9A_Ethernet31/1
   neighbor 172.17.4.107 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.107 remote-as 64909
   neighbor 172.17.4.107 description DC1-POD1-LEAF9A_Ethernet31/2
   neighbor 172.17.4.137 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.137 remote-as 64909
   neighbor 172.17.4.137 description DC1-POD1-LEAF9B_Ethernet31/1
   neighbor 172.17.4.139 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.139 remote-as 64909
   neighbor 172.17.4.139 description DC1-POD1-LEAF9B_Ethernet31/2
   neighbor 172.17.4.169 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.169 remote-as 64910
   neighbor 172.17.4.169 description DC1-POD1-LEAF10A_Ethernet31/1
   neighbor 172.17.4.171 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.171 remote-as 64910
   neighbor 172.17.4.171 description DC1-POD1-LEAF10A_Ethernet31/2
   neighbor 172.17.4.201 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.201 remote-as 64910
   neighbor 172.17.4.201 description DC1-POD1-LEAF10B_Ethernet31/1
   neighbor 172.17.4.203 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.203 remote-as 64910
   neighbor 172.17.4.203 description DC1-POD1-LEAF10B_Ethernet31/2
   neighbor 172.17.4.233 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.233 remote-as 64911
   neighbor 172.17.4.233 description DC1-POD1-LEAF11A_Ethernet31/1
   neighbor 172.17.4.235 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.4.235 remote-as 64911
   neighbor 172.17.4.235 description DC1-POD1-LEAF11A_Ethernet31/2
   neighbor 172.17.5.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.9 remote-as 64911
   neighbor 172.17.5.9 description DC1-POD1-LEAF11B_Ethernet31/1
   neighbor 172.17.5.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.11 remote-as 64911
   neighbor 172.17.5.11 description DC1-POD1-LEAF11B_Ethernet31/2
   neighbor 172.17.5.41 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.41 remote-as 64912
   neighbor 172.17.5.41 description DC1-POD1-LEAF12A_Ethernet31/1
   neighbor 172.17.5.43 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.43 remote-as 64912
   neighbor 172.17.5.43 description DC1-POD1-LEAF12A_Ethernet31/2
   neighbor 172.17.5.73 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.73 remote-as 64912
   neighbor 172.17.5.73 description DC1-POD1-LEAF12B_Ethernet31/1
   neighbor 172.17.5.75 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.75 remote-as 64912
   neighbor 172.17.5.75 description DC1-POD1-LEAF12B_Ethernet31/2
   neighbor 172.17.5.105 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.105 remote-as 64913
   neighbor 172.17.5.105 description DC1-POD1-LEAF13A_Ethernet31/1
   neighbor 172.17.5.107 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.107 remote-as 64913
   neighbor 172.17.5.107 description DC1-POD1-LEAF13A_Ethernet31/2
   neighbor 172.17.5.137 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.137 remote-as 64913
   neighbor 172.17.5.137 description DC1-POD1-LEAF13B_Ethernet31/1
   neighbor 172.17.5.139 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.139 remote-as 64913
   neighbor 172.17.5.139 description DC1-POD1-LEAF13B_Ethernet31/2
   neighbor 172.17.5.169 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.169 remote-as 64914
   neighbor 172.17.5.169 description DC1-POD1-LEAF14A_Ethernet31/1
   neighbor 172.17.5.171 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.171 remote-as 64914
   neighbor 172.17.5.171 description DC1-POD1-LEAF14A_Ethernet31/2
   neighbor 172.17.5.201 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.201 remote-as 64914
   neighbor 172.17.5.201 description DC1-POD1-LEAF14B_Ethernet31/1
   neighbor 172.17.5.203 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.5.203 remote-as 64914
   neighbor 172.17.5.203 description DC1-POD1-LEAF14B_Ethernet31/2
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
