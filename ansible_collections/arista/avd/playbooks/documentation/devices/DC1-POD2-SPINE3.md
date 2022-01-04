# DC1-POD2-SPINE3
# Table of Contents
<!-- toc -->

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

<!-- toc -->
# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 10.6.33.3/24 | 10.6.1.1 |

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
   ip address 10.6.33.3/24
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---------- | ---------- |
| default | true |

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
| - | AMS DC1 DC1_POD2 DC1-POD2-SPINE3 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD2 DC1-POD2-SPINE3
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

### Global Spanning-Tree Settings


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
| Ethernet1/1 | P2P_LINK_TO_DC1-POD2-LEAF1A_Ethernet31/1 | routed | - | 172.17.2.4/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD2-LEAF1B_Ethernet31/1 | routed | - | 172.17.2.12/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD2-LEAF2A_Ethernet31/1 | routed | - | 172.17.2.20/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD2-LEAF2B_Ethernet31/1 | routed | - | 172.17.2.28/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD2-LEAF3A_Ethernet31/1 | routed | - | 172.17.2.36/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD2-LEAF3B_Ethernet31/1 | routed | - | 172.17.2.44/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD2-LEAF4A_Ethernet31/1 | routed | - | 172.17.2.52/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD2-LEAF4B_Ethernet31/1 | routed | - | 172.17.2.60/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-POD2-LEAF5A_Ethernet31/1 | routed | - | 172.17.2.68/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC1-POD2-LEAF5B_Ethernet31/1 | routed | - | 172.17.2.76/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC1-POD2-LEAF6A_Ethernet31/1 | routed | - | 172.17.2.84/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC1-POD2-LEAF6B_Ethernet31/1 | routed | - | 172.17.2.92/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC1-POD2-LEAF7A_Ethernet31/1 | routed | - | 172.17.2.100/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC1-POD2-LEAF7B_Ethernet31/1 | routed | - | 172.17.2.108/31 | default | 9214 | false | - | - |
| Ethernet15/1 | P2P_LINK_TO_DC1-POD2-LEAF8A_Ethernet31/1 | routed | - | 172.17.2.116/31 | default | 9214 | false | - | - |
| Ethernet16/1 | P2P_LINK_TO_DC1-POD2-LEAF8B_Ethernet31/1 | routed | - | 172.17.2.124/31 | default | 9214 | false | - | - |
| Ethernet17/1 | P2P_LINK_TO_DC1-POD2-LEAF9A_Ethernet31/1 | routed | - | 172.17.2.132/31 | default | 9214 | false | - | - |
| Ethernet18/1 | P2P_LINK_TO_DC1-POD2-LEAF9B_Ethernet31/1 | routed | - | 172.17.2.140/31 | default | 9214 | false | - | - |
| Ethernet19/1 | P2P_LINK_TO_DC1-POD2-LEAF10A_Ethernet31/1 | routed | - | 172.17.2.148/31 | default | 9214 | false | - | - |
| Ethernet20/1 | P2P_LINK_TO_DC1-POD2-LEAF10B_Ethernet31/1 | routed | - | 172.17.2.156/31 | default | 9214 | false | - | - |
| Ethernet21/1 | P2P_LINK_TO_DC1-POD2-LEAF11A_Ethernet31/1 | routed | - | 172.17.2.164/31 | default | 9214 | false | - | - |
| Ethernet22/1 | P2P_LINK_TO_DC1-POD2-LEAF11B_Ethernet31/1 | routed | - | 172.17.2.172/31 | default | 9214 | false | - | - |
| Ethernet23/1 | P2P_LINK_TO_DC1-POD2-LEAF12A_Ethernet31/1 | routed | - | 172.17.2.180/31 | default | 9214 | false | - | - |
| Ethernet24/1 | P2P_LINK_TO_DC1-POD2-LEAF12B_Ethernet31/1 | routed | - | 172.17.2.188/31 | default | 9214 | false | - | - |
| Ethernet25/1 | P2P_LINK_TO_DC1-POD2-LEAF13A_Ethernet31/1 | routed | - | 172.17.2.196/31 | default | 9214 | false | - | - |
| Ethernet26/1 | P2P_LINK_TO_DC1-POD2-LEAF13B_Ethernet31/1 | routed | - | 172.17.2.204/31 | default | 9214 | false | - | - |
| Ethernet27/1 | P2P_LINK_TO_DC1-POD2-LEAF14A_Ethernet31/1 | routed | - | 172.17.2.212/31 | default | 9214 | false | - | - |
| Ethernet28/1 | P2P_LINK_TO_DC1-POD2-LEAF14B_Ethernet31/1 | routed | - | 172.17.2.220/31 | default | 9214 | false | - | - |
| Ethernet29/1 | P2P_LINK_TO_SUPER-SPINE1_Ethernet7/1 | routed | - | 172.16.2.5/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_SUPER-SPINE2_Ethernet7/1 | routed | - | 172.16.2.69/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet7/1 | routed | - | 172.16.2.133/31 | default | 9214 | false | - | - |
| Ethernet32/1 | P2P_LINK_TO_SUPER-SPINE4_Ethernet7/1 | routed | - | 172.16.2.197/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD2-LEAF1A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.4/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD2-LEAF1B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.12/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD2-LEAF2A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.20/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD2-LEAF2B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.28/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD2-LEAF3A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.36/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD2-LEAF3B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.44/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD2-LEAF4A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.52/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD2-LEAF4B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.60/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-POD2-LEAF5A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.68/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC1-POD2-LEAF5B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.76/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC1-POD2-LEAF6A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.84/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC1-POD2-LEAF6B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.92/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC1-POD2-LEAF7A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.100/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC1-POD2-LEAF7B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.108/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet15/1
   description P2P_LINK_TO_DC1-POD2-LEAF8A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.116/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet16/1
   description P2P_LINK_TO_DC1-POD2-LEAF8B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.124/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet17/1
   description P2P_LINK_TO_DC1-POD2-LEAF9A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.132/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet18/1
   description P2P_LINK_TO_DC1-POD2-LEAF9B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.140/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet19/1
   description P2P_LINK_TO_DC1-POD2-LEAF10A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.148/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet20/1
   description P2P_LINK_TO_DC1-POD2-LEAF10B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.156/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet21/1
   description P2P_LINK_TO_DC1-POD2-LEAF11A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.164/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet22/1
   description P2P_LINK_TO_DC1-POD2-LEAF11B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.172/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet23/1
   description P2P_LINK_TO_DC1-POD2-LEAF12A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.180/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet24/1
   description P2P_LINK_TO_DC1-POD2-LEAF12B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.188/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet25/1
   description P2P_LINK_TO_DC1-POD2-LEAF13A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.196/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet26/1
   description P2P_LINK_TO_DC1-POD2-LEAF13B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.204/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet27/1
   description P2P_LINK_TO_DC1-POD2-LEAF14A_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.212/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet28/1
   description P2P_LINK_TO_DC1-POD2-LEAF14B_Ethernet31/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.220/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/1
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet7/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.5/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet7/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.69/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet7/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.133/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/1
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet7/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.197/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.29.3/32 |

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
   ip address 10.4.29.3/32
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
| default | true|| mgmt | false |

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
| default | false || mgmt | false |


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
| 65001.200|  10.4.29.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 16 ecmp 16 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Send-community | Maximum-routes |
| -------- | --------- | --- | -------------- | -------------- |
| 172.16.2.4 | 64101 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.68 | 64102 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.132 | 64103 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.196 | 64104 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.5 | 65112.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.13 | 65112.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.21 | 65112.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.29 | 65112.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.37 | 65112.300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.45 | 65112.300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.53 | 65112.400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.61 | 65112.400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.69 | 65112.500 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.77 | 65112.500 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.85 | 65112.600 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.93 | 65112.600 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.101 | 65112.700 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.109 | 65112.700 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.117 | 65112.800 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.125 | 65112.800 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.133 | 65112.900 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.141 | 65112.900 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.149 | 65112.1000 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.157 | 65112.1000 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.165 | 65112.1100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.173 | 65112.1100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.181 | 65112.1200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.189 | 65112.1200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.197 | 65112.1300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.205 | 65112.1300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.213 | 65112.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.221 | 65112.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

#### Router BGP EVPN VRFs

### Router BGP Device Configuration

```eos
!
router bgp 65001.200
   router-id 10.4.29.3
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 16 ecmp 16
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.2.4 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.4 remote-as 64101
   neighbor 172.16.2.4 description SUPER-SPINE1_Ethernet7/1
   neighbor 172.16.2.68 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.68 remote-as 64102
   neighbor 172.16.2.68 description SUPER-SPINE2_Ethernet7/1
   neighbor 172.16.2.132 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.132 remote-as 64103
   neighbor 172.16.2.132 description SUPER-SPINE3_Ethernet7/1
   neighbor 172.16.2.196 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.196 remote-as 64104
   neighbor 172.16.2.196 description SUPER-SPINE4_Ethernet7/1
   neighbor 172.17.2.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.5 remote-as 65112.100
   neighbor 172.17.2.5 description DC1-POD2-LEAF1A_Ethernet31/1
   neighbor 172.17.2.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.13 remote-as 65112.100
   neighbor 172.17.2.13 description DC1-POD2-LEAF1B_Ethernet31/1
   neighbor 172.17.2.21 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.21 remote-as 65112.200
   neighbor 172.17.2.21 description DC1-POD2-LEAF2A_Ethernet31/1
   neighbor 172.17.2.29 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.29 remote-as 65112.200
   neighbor 172.17.2.29 description DC1-POD2-LEAF2B_Ethernet31/1
   neighbor 172.17.2.37 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.37 remote-as 65112.300
   neighbor 172.17.2.37 description DC1-POD2-LEAF3A_Ethernet31/1
   neighbor 172.17.2.45 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.45 remote-as 65112.300
   neighbor 172.17.2.45 description DC1-POD2-LEAF3B_Ethernet31/1
   neighbor 172.17.2.53 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.53 remote-as 65112.400
   neighbor 172.17.2.53 description DC1-POD2-LEAF4A_Ethernet31/1
   neighbor 172.17.2.61 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.61 remote-as 65112.400
   neighbor 172.17.2.61 description DC1-POD2-LEAF4B_Ethernet31/1
   neighbor 172.17.2.69 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.69 remote-as 65112.500
   neighbor 172.17.2.69 description DC1-POD2-LEAF5A_Ethernet31/1
   neighbor 172.17.2.77 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.77 remote-as 65112.500
   neighbor 172.17.2.77 description DC1-POD2-LEAF5B_Ethernet31/1
   neighbor 172.17.2.85 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.85 remote-as 65112.600
   neighbor 172.17.2.85 description DC1-POD2-LEAF6A_Ethernet31/1
   neighbor 172.17.2.93 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.93 remote-as 65112.600
   neighbor 172.17.2.93 description DC1-POD2-LEAF6B_Ethernet31/1
   neighbor 172.17.2.101 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.101 remote-as 65112.700
   neighbor 172.17.2.101 description DC1-POD2-LEAF7A_Ethernet31/1
   neighbor 172.17.2.109 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.109 remote-as 65112.700
   neighbor 172.17.2.109 description DC1-POD2-LEAF7B_Ethernet31/1
   neighbor 172.17.2.117 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.117 remote-as 65112.800
   neighbor 172.17.2.117 description DC1-POD2-LEAF8A_Ethernet31/1
   neighbor 172.17.2.125 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.125 remote-as 65112.800
   neighbor 172.17.2.125 description DC1-POD2-LEAF8B_Ethernet31/1
   neighbor 172.17.2.133 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.133 remote-as 65112.900
   neighbor 172.17.2.133 description DC1-POD2-LEAF9A_Ethernet31/1
   neighbor 172.17.2.141 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.141 remote-as 65112.900
   neighbor 172.17.2.141 description DC1-POD2-LEAF9B_Ethernet31/1
   neighbor 172.17.2.149 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.149 remote-as 65112.1000
   neighbor 172.17.2.149 description DC1-POD2-LEAF10A_Ethernet31/1
   neighbor 172.17.2.157 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.157 remote-as 65112.1000
   neighbor 172.17.2.157 description DC1-POD2-LEAF10B_Ethernet31/1
   neighbor 172.17.2.165 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.165 remote-as 65112.1100
   neighbor 172.17.2.165 description DC1-POD2-LEAF11A_Ethernet31/1
   neighbor 172.17.2.173 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.173 remote-as 65112.1100
   neighbor 172.17.2.173 description DC1-POD2-LEAF11B_Ethernet31/1
   neighbor 172.17.2.181 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.181 remote-as 65112.1200
   neighbor 172.17.2.181 description DC1-POD2-LEAF12A_Ethernet31/1
   neighbor 172.17.2.189 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.189 remote-as 65112.1200
   neighbor 172.17.2.189 description DC1-POD2-LEAF12B_Ethernet31/1
   neighbor 172.17.2.197 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.197 remote-as 65112.1300
   neighbor 172.17.2.197 description DC1-POD2-LEAF13A_Ethernet31/1
   neighbor 172.17.2.205 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.205 remote-as 65112.1300
   neighbor 172.17.2.205 description DC1-POD2-LEAF13B_Ethernet31/1
   neighbor 172.17.2.213 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.213 remote-as 65112.1400
   neighbor 172.17.2.213 description DC1-POD2-LEAF14A_Ethernet31/1
   neighbor 172.17.2.221 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.221 remote-as 65112.1400
   neighbor 172.17.2.221 description DC1-POD2-LEAF14B_Ethernet31/1
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
| 10 | permit 10.4.29.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.29.0/24 eq 32
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
