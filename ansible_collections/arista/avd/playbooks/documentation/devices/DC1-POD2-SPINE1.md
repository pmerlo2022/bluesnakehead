# DC1-POD2-SPINE1
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
| Management0 | oob_management | oob | mgmt | 10.6.33.1/24 | 10.6.1.1 |

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
   ip address 10.6.33.1/24
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
| - | AMS DC1 DC1_POD2 DC1-POD2-SPINE1 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD2 DC1-POD2-SPINE1
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
| Ethernet1/1 | P2P_LINK_TO_DC1-POD2-LEAF1A_Ethernet29/1 | routed | - | 172.17.2.0/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD2-LEAF1B_Ethernet29/1 | routed | - | 172.17.2.8/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD2-LEAF2A_Ethernet29/1 | routed | - | 172.17.2.16/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD2-LEAF2B_Ethernet29/1 | routed | - | 172.17.2.24/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD2-LEAF3A_Ethernet29/1 | routed | - | 172.17.2.32/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD2-LEAF3B_Ethernet29/1 | routed | - | 172.17.2.40/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD2-LEAF4A_Ethernet29/1 | routed | - | 172.17.2.48/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD2-LEAF4B_Ethernet29/1 | routed | - | 172.17.2.56/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-POD2-LEAF5A_Ethernet29/1 | routed | - | 172.17.2.64/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC1-POD2-LEAF5B_Ethernet29/1 | routed | - | 172.17.2.72/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC1-POD2-LEAF6A_Ethernet29/1 | routed | - | 172.17.2.80/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC1-POD2-LEAF6B_Ethernet29/1 | routed | - | 172.17.2.88/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC1-POD2-LEAF7A_Ethernet29/1 | routed | - | 172.17.2.96/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC1-POD2-LEAF7B_Ethernet29/1 | routed | - | 172.17.2.104/31 | default | 9214 | false | - | - |
| Ethernet15/1 | P2P_LINK_TO_DC1-POD2-LEAF8A_Ethernet29/1 | routed | - | 172.17.2.112/31 | default | 9214 | false | - | - |
| Ethernet16/1 | P2P_LINK_TO_DC1-POD2-LEAF8B_Ethernet29/1 | routed | - | 172.17.2.120/31 | default | 9214 | false | - | - |
| Ethernet17/1 | P2P_LINK_TO_DC1-POD2-LEAF9A_Ethernet29/1 | routed | - | 172.17.2.128/31 | default | 9214 | false | - | - |
| Ethernet18/1 | P2P_LINK_TO_DC1-POD2-LEAF9B_Ethernet29/1 | routed | - | 172.17.2.136/31 | default | 9214 | false | - | - |
| Ethernet19/1 | P2P_LINK_TO_DC1-POD2-LEAF10A_Ethernet29/1 | routed | - | 172.17.2.144/31 | default | 9214 | false | - | - |
| Ethernet20/1 | P2P_LINK_TO_DC1-POD2-LEAF10B_Ethernet29/1 | routed | - | 172.17.2.152/31 | default | 9214 | false | - | - |
| Ethernet21/1 | P2P_LINK_TO_DC1-POD2-LEAF11A_Ethernet29/1 | routed | - | 172.17.2.160/31 | default | 9214 | false | - | - |
| Ethernet22/1 | P2P_LINK_TO_DC1-POD2-LEAF11B_Ethernet29/1 | routed | - | 172.17.2.168/31 | default | 9214 | false | - | - |
| Ethernet23/1 | P2P_LINK_TO_DC1-POD2-LEAF12A_Ethernet29/1 | routed | - | 172.17.2.176/31 | default | 9214 | false | - | - |
| Ethernet24/1 | P2P_LINK_TO_DC1-POD2-LEAF12B_Ethernet29/1 | routed | - | 172.17.2.184/31 | default | 9214 | false | - | - |
| Ethernet25/1 | P2P_LINK_TO_DC1-POD2-LEAF13A_Ethernet29/1 | routed | - | 172.17.2.192/31 | default | 9214 | false | - | - |
| Ethernet26/1 | P2P_LINK_TO_DC1-POD2-LEAF13B_Ethernet29/1 | routed | - | 172.17.2.200/31 | default | 9214 | false | - | - |
| Ethernet27/1 | P2P_LINK_TO_DC1-POD2-LEAF14A_Ethernet29/1 | routed | - | 172.17.2.208/31 | default | 9214 | false | - | - |
| Ethernet28/1 | P2P_LINK_TO_DC1-POD2-LEAF14B_Ethernet29/1 | routed | - | 172.17.2.216/31 | default | 9214 | false | - | - |
| Ethernet29/1 | P2P_LINK_TO_SUPER-SPINE1_Ethernet5/1 | routed | - | 172.16.2.1/31 | default | 9214 | false | - | - |
| Ethernet29/2 | P2P_LINK_TO_SUPER-SPINE1_Ethernet5/2 | routed | - | 172.16.2.33/31 | default | 9214 | false | - | - |
| Ethernet29/3 | P2P_LINK_TO_SUPER-SPINE2_Ethernet5/3 | routed | - | 172.16.2.65/31 | default | 9214 | false | - | - |
| Ethernet29/4 | P2P_LINK_TO_SUPER-SPINE2_Ethernet5/4 | routed | - | 172.16.2.97/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet6/1 | routed | - | 172.16.2.129/31 | default | 9214 | false | - | - |
| Ethernet30/2 | P2P_LINK_TO_SUPER-SPINE3_Ethernet6/2 | routed | - | 172.16.2.161/31 | default | 9214 | false | - | - |
| Ethernet30/3 | P2P_LINK_TO_SUPER-SPINE4_Ethernet6/3 | routed | - | 172.16.2.193/31 | default | 9214 | false | - | - |
| Ethernet30/4 | P2P_LINK_TO_SUPER-SPINE4_Ethernet6/4 | routed | - | 172.16.2.225/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD2-LEAF1A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.0/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD2-LEAF1B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.8/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD2-LEAF2A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.16/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD2-LEAF2B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.24/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD2-LEAF3A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.32/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD2-LEAF3B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.40/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD2-LEAF4A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.48/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD2-LEAF4B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.56/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-POD2-LEAF5A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.64/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC1-POD2-LEAF5B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.72/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC1-POD2-LEAF6A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.80/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC1-POD2-LEAF6B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.88/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC1-POD2-LEAF7A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.96/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC1-POD2-LEAF7B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.104/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet15/1
   description P2P_LINK_TO_DC1-POD2-LEAF8A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.112/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet16/1
   description P2P_LINK_TO_DC1-POD2-LEAF8B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.120/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet17/1
   description P2P_LINK_TO_DC1-POD2-LEAF9A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.128/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet18/1
   description P2P_LINK_TO_DC1-POD2-LEAF9B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.136/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet19/1
   description P2P_LINK_TO_DC1-POD2-LEAF10A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.144/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet20/1
   description P2P_LINK_TO_DC1-POD2-LEAF10B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.152/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet21/1
   description P2P_LINK_TO_DC1-POD2-LEAF11A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.160/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet22/1
   description P2P_LINK_TO_DC1-POD2-LEAF11B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.168/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet23/1
   description P2P_LINK_TO_DC1-POD2-LEAF12A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.176/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet24/1
   description P2P_LINK_TO_DC1-POD2-LEAF12B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.184/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet25/1
   description P2P_LINK_TO_DC1-POD2-LEAF13A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.192/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet26/1
   description P2P_LINK_TO_DC1-POD2-LEAF13B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.200/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet27/1
   description P2P_LINK_TO_DC1-POD2-LEAF14A_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.208/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet28/1
   description P2P_LINK_TO_DC1-POD2-LEAF14B_Ethernet29/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.2.216/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/1
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet5/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.1/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/2
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet5/2
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.33/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/3
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet5/3
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.65/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/4
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet5/4
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.97/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.129/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/2
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet6/2
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.161/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/3
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet6/3
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.193/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/4
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet6/4
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.225/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.29.1/32 |

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
   ip address 10.4.29.1/32
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
| 65001.200|  10.4.29.1 |

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
| 172.16.2.0 | 64101 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.32 | 64101 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.64 | 64102 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.96 | 64102 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.128 | 64103 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.160 | 64103 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.192 | 64104 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.224 | 64104 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.1 | 65112.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.9 | 65112.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.17 | 65112.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.25 | 65112.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.33 | 65112.300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.41 | 65112.300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.49 | 65112.400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.57 | 65112.400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.65 | 65112.500 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.73 | 65112.500 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.81 | 65112.600 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.89 | 65112.600 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.97 | 65112.700 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.105 | 65112.700 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.113 | 65112.800 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.121 | 65112.800 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.129 | 65112.900 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.137 | 65112.900 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.145 | 65112.1000 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.153 | 65112.1000 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.161 | 65112.1100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.169 | 65112.1100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.177 | 65112.1200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.185 | 65112.1200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.193 | 65112.1300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.201 | 65112.1300 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.209 | 65112.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.17.2.217 | 65112.1400 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

#### Router BGP EVPN VRFs

### Router BGP Device Configuration

```eos
!
router bgp 65001.200
   router-id 10.4.29.1
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 16 ecmp 16
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.2.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.0 remote-as 64101
   neighbor 172.16.2.0 description SUPER-SPINE1_Ethernet5/1
   neighbor 172.16.2.32 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.32 remote-as 64101
   neighbor 172.16.2.32 description SUPER-SPINE1_Ethernet5/2
   neighbor 172.16.2.64 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.64 remote-as 64102
   neighbor 172.16.2.64 description SUPER-SPINE2_Ethernet5/3
   neighbor 172.16.2.96 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.96 remote-as 64102
   neighbor 172.16.2.96 description SUPER-SPINE2_Ethernet5/4
   neighbor 172.16.2.128 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.128 remote-as 64103
   neighbor 172.16.2.128 description SUPER-SPINE3_Ethernet6/1
   neighbor 172.16.2.160 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.160 remote-as 64103
   neighbor 172.16.2.160 description SUPER-SPINE3_Ethernet6/2
   neighbor 172.16.2.192 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.192 remote-as 64104
   neighbor 172.16.2.192 description SUPER-SPINE4_Ethernet6/3
   neighbor 172.16.2.224 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.224 remote-as 64104
   neighbor 172.16.2.224 description SUPER-SPINE4_Ethernet6/4
   neighbor 172.17.2.1 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.1 remote-as 65112.100
   neighbor 172.17.2.1 description DC1-POD2-LEAF1A_Ethernet29/1
   neighbor 172.17.2.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.9 remote-as 65112.100
   neighbor 172.17.2.9 description DC1-POD2-LEAF1B_Ethernet29/1
   neighbor 172.17.2.17 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.17 remote-as 65112.200
   neighbor 172.17.2.17 description DC1-POD2-LEAF2A_Ethernet29/1
   neighbor 172.17.2.25 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.25 remote-as 65112.200
   neighbor 172.17.2.25 description DC1-POD2-LEAF2B_Ethernet29/1
   neighbor 172.17.2.33 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.33 remote-as 65112.300
   neighbor 172.17.2.33 description DC1-POD2-LEAF3A_Ethernet29/1
   neighbor 172.17.2.41 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.41 remote-as 65112.300
   neighbor 172.17.2.41 description DC1-POD2-LEAF3B_Ethernet29/1
   neighbor 172.17.2.49 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.49 remote-as 65112.400
   neighbor 172.17.2.49 description DC1-POD2-LEAF4A_Ethernet29/1
   neighbor 172.17.2.57 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.57 remote-as 65112.400
   neighbor 172.17.2.57 description DC1-POD2-LEAF4B_Ethernet29/1
   neighbor 172.17.2.65 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.65 remote-as 65112.500
   neighbor 172.17.2.65 description DC1-POD2-LEAF5A_Ethernet29/1
   neighbor 172.17.2.73 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.73 remote-as 65112.500
   neighbor 172.17.2.73 description DC1-POD2-LEAF5B_Ethernet29/1
   neighbor 172.17.2.81 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.81 remote-as 65112.600
   neighbor 172.17.2.81 description DC1-POD2-LEAF6A_Ethernet29/1
   neighbor 172.17.2.89 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.89 remote-as 65112.600
   neighbor 172.17.2.89 description DC1-POD2-LEAF6B_Ethernet29/1
   neighbor 172.17.2.97 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.97 remote-as 65112.700
   neighbor 172.17.2.97 description DC1-POD2-LEAF7A_Ethernet29/1
   neighbor 172.17.2.105 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.105 remote-as 65112.700
   neighbor 172.17.2.105 description DC1-POD2-LEAF7B_Ethernet29/1
   neighbor 172.17.2.113 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.113 remote-as 65112.800
   neighbor 172.17.2.113 description DC1-POD2-LEAF8A_Ethernet29/1
   neighbor 172.17.2.121 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.121 remote-as 65112.800
   neighbor 172.17.2.121 description DC1-POD2-LEAF8B_Ethernet29/1
   neighbor 172.17.2.129 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.129 remote-as 65112.900
   neighbor 172.17.2.129 description DC1-POD2-LEAF9A_Ethernet29/1
   neighbor 172.17.2.137 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.137 remote-as 65112.900
   neighbor 172.17.2.137 description DC1-POD2-LEAF9B_Ethernet29/1
   neighbor 172.17.2.145 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.145 remote-as 65112.1000
   neighbor 172.17.2.145 description DC1-POD2-LEAF10A_Ethernet29/1
   neighbor 172.17.2.153 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.153 remote-as 65112.1000
   neighbor 172.17.2.153 description DC1-POD2-LEAF10B_Ethernet29/1
   neighbor 172.17.2.161 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.161 remote-as 65112.1100
   neighbor 172.17.2.161 description DC1-POD2-LEAF11A_Ethernet29/1
   neighbor 172.17.2.169 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.169 remote-as 65112.1100
   neighbor 172.17.2.169 description DC1-POD2-LEAF11B_Ethernet29/1
   neighbor 172.17.2.177 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.177 remote-as 65112.1200
   neighbor 172.17.2.177 description DC1-POD2-LEAF12A_Ethernet29/1
   neighbor 172.17.2.185 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.185 remote-as 65112.1200
   neighbor 172.17.2.185 description DC1-POD2-LEAF12B_Ethernet29/1
   neighbor 172.17.2.193 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.193 remote-as 65112.1300
   neighbor 172.17.2.193 description DC1-POD2-LEAF13A_Ethernet29/1
   neighbor 172.17.2.201 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.201 remote-as 65112.1300
   neighbor 172.17.2.201 description DC1-POD2-LEAF13B_Ethernet29/1
   neighbor 172.17.2.209 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.209 remote-as 65112.1400
   neighbor 172.17.2.209 description DC1-POD2-LEAF14A_Ethernet29/1
   neighbor 172.17.2.217 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.2.217 remote-as 65112.1400
   neighbor 172.17.2.217 description DC1-POD2-LEAF14B_Ethernet29/1
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
